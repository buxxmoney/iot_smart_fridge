# 🧊 IoT Smart Fridge Tracker

An affordable, scalable IoT solution that turns a standard fridge into a smart appliance using image recognition, sensor tracking, and cloud services. Built to reduce food waste, notify users of fridge failures, and suggest recipes based on real-time inventory.

> **Team Members**: Erik Wrysinski, Jack Gaul, Mubashir Hussain, Sebastian Buxman, Swarom Saurabh Muley  
> **Course**: COEN 243 Project

---

## 📌 Problem Statement

Consumers often:
- Re-purchase items they already have.
- Waste food due to forgotten expiration dates.
- Have no visibility into fridge contents when shopping.
- Discover fridge failures too late after temperature spikes.

---

## 🚀 Our Solution

A Raspberry Pi-powered IoT system that:
- Uses a CSI camera to capture images of fridge contents.
- Performs object detection to auto-update inventory.
- Predicts expiration dates based on public data and sensor readings.
- Sends notifications when items are about to expire or when temperature rises unexpectedly.
- Displays data through a user-friendly mobile app and web dashboard.

---

## 🛠️ Tools, Tech & Hardware

### 🔧 Hardware
- **Raspberry Pi** with CSI Camera (5MP, 160° FOV)
- **DHT22 Sensor** for temperature and humidity

### 🧑‍💻 Software & Services
- **Operating System**: Linux
- **Backend**: Flask on AWS EC2
- **Database**: AWS DynamoDB
- **Notifications**: Twilio / SendGrid
- **APIs**: OpenAI (for recipe suggestions)
- **Computer Vision**: OpenCV, Image Classification Models

---

## 🔄 System Architecture

- **Edge Device**: Raspberry Pi captures sensor and camera data.
- **Web Server**: Flask API hosted on AWS EC2.
- **Database**: DynamoDB stores fridge inventory and environmental stats.
- **Mobile App**: Swift-based frontend for viewing contents, recipes, and climate history.

---

## 📱 Key Features

- ✅ **Image-Based Inventory Tracking**  
  Automatically adds items to inventory via camera scans with classification and timestamping.

- 📷 **Real-Time Fridge View**  
  Snapshots are viewable from mobile and web.

- 🕒 **Expiration Date Prediction**  
  Estimates lifespan based on public food databases.

- 🔔 **Temperature Alerts**  
  Notifies users when the fridge temp goes above threshold.

- 📡 **Cloud-Based Dashboard**  
  Fridge status, climate trends, and recipes all in one place.

- 🍽️ **Meal Suggestions**  
  AI-generated recipes based on current fridge contents.

---

## 💡 Key Learnings

- Open-source classification models are limited without custom training.
- Building rule-based systems was more practical than ML-based expiration prediction due to lack of labeled data.
- Configuring secure IoT-cloud communications was crucial.
- Edge deployment with live sensors and camera required careful resource balancing.

---

## 🧠 Future Improvements

- Train custom food recognition models for improved accuracy.
- Implement a learned expiration prediction model.
- Design a hardware enclosure with auto-capture on fridge door events.
- Improve durability and adaptability across different fridge types.
- Experiment with ideal sensor placements for reliable climate tracking.

---

## 🧑‍🤝‍🧑 Task Distribution

| Team Member     | Responsibility |
|-----------------|----------------|
| **Erik**        | Raspberry Pi integration, photo capture, cloud upload |
| **Jack**        | Backend infra, AWS setup, Twilio alerts, OpenAI integration |
| **Mubashir**    | Image classification model, Raspberry Pi camera integration |
| **Sebastian**   | Temperature/humidity tracking, expiration prediction logic |
| **Swarom**      | Swift mobile app development and integration |

---

## 📸 Screenshots

- **Home Page**: Real-time temperature, humidity, and snapshot.
- **Health Page**: Graphs of climate stats over time.
- **Recipe Page**: Suggestions based on inventory.
- **Fridge Page**: Auto-classified item photos.

---

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
