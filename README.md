# fridge_cam
All code for the fridge camera project


<p align="middle">
  <img src="/Assets/home.png" width="200" height="400" style="margin-right: 20px;">
  <img src="/Assets/health.png" width="200" height="400" style="margin-left: 10px; margin-right: 10px;">
  <img src="/Assets/fridge.png" width="200" height="400" style="margin-left: 20px;">
</p>


## Server Endpoints 

- `/get_item_photo`
  - returns the image URL

- `/upload` (post)
  - uploads classified image into s3

- `/upload_fridge_conditions` (post)
  - stores temperature & humidity of the fridge

- `/list_fridge_items/<account_id>` (get)
  - list all items in the fridge

- `/encrypted_api_key_header` (get)
  - recieves the encrypted api key from the client in the header and decrypts it

- `/public_key` (get)
  - sends the public key to the client

- `/current_fridge_photo` (post,get)
  - upload/return the current photo of the fridge