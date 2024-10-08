import subprocess
import cv2
from inference import get_roboflow_model
import supervision as sv

# Function to capture an image using libcamera-still
def capture_image(image_path):
    capture_command = ['libcamera-still', '-o',image_path]
    try:
        subprocess.run(capture_command, check=True)
        print(f"Image captured and saved as {image_path}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Path for the captured image
image_file = 'captured_image.jpg'

# Capture an image
capture_image(image_file)

# Read the captured image
image = cv2.imread(image_file)
if image is None:
    raise Exception(f"Failed to load image from {image_file}")

# Load a pre-trained yolov8n model
model = get_roboflow_model(model_id="aicook-lcv4d/3")

# Run inference on the captured image
results = model.infer(image)
print(results)

# Load the results into the supervision Detections API
detections = sv.Detections.from_inference(results[0].dict(by_alias=True, exclude_none=True))

# Create supervision annotators
bounding_box_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()

# Annotate the image with the inference results
annotated_image = bounding_box_annotator.annotate(scene=image, detections=detections)
annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)

# Convert the annotated image from RGB to BGR format before saving with OpenCV
#annotated_image_bgr = cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR)

# Save the annotated image locally
annotated_image_file = 'annotated_image.jpg'
cv2.imwrite(annotated_image_file, annotated_image)
print(f"Annotated image saved as {annotated_image_file}")
