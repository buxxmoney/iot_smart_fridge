from encryption_utils import *
from client_endpoint_test import *
import time
import board
import adafruit_dht
import subprocess
import cv2


# Initialize the DHT22 sensor
dhtDevice = adafruit_dht.DHT22(board.D4)

jacks_device = "http://52.52.9.39:5000"
prod_server_url = "http://52.8.39.250:5000"

# Function to capture an image using libcamera-still
def capture_image(image_path):
    capture_command = ['libcamera-still', '-o', image_path, '--timeout', '800', '--width', '1920', '--height', '1080']
    try:
        subprocess.run(capture_command, check=True)
        print(f"Image captured and saved as {image_path}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


# Maximum number of retries
MAX_RETRIES = 10

# Delay between retries in seconds
RETRY_DELAY = .5

def read_dht22(dht_device):
    for attempt in range(MAX_RETRIES):
        try:
            # Attempt to read the temperature and humidity from the sensor
            temperature_c = dht_device.temperature
            humidity = dht_device.humidity
            if temperature_c is not None and humidity is not None:
                return temperature_c, humidity
            else:
                # Data was None, which sometimes happens, so retry
                print(f"Attempt {attempt + 1} of {MAX_RETRIES}: Got None from the sensor, retrying...")
                time.sleep(RETRY_DELAY)
        except RuntimeError as e:
            # Log the error and wait before retrying
            print(f"Attempt {attempt + 1} of {MAX_RETRIES}: {e}, retrying...")
            time.sleep(RETRY_DELAY)

    # If we reach this point, all retries have failed
    print("Failed to read from DHT22 sensor after maximum retries.")
    return None, None  # Indicate failure


# Main loop
try:
    while True:
        # Path for the captured image - consider adding a timestamp or unique identifier to filename if desired
        image_file = 'captured_image.jpg'

        # Capture a fresh image
        capture_image(image_file)

        # Read fresh sensor data
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        temperature_f = (temperature_c * 9 / 5) + 32

        # Upload sensor data
        response = humid_temp_upload(jacks_device, str(temperature_f), str(humidity), b'YourCameraAPIKey')
        print("Sensor data uploaded successfully.")

        # Upload the newly captured image
        response = fridge_image_upload(jacks_device, str(101095), image_file)
        print("Image uploaded successfully.")

        print("Temp: {:.1f} F    Humidity: {}% ".format(temperature_f, humidity))
        print(response)

        # Wait for 900 seconds before capturing a new image and reading sensor data again
        time.sleep(900)

except KeyboardInterrupt:
    print("Process terminated by user.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
