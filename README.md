#  DroneVision

### YOLO-Based Drone Detection System

DroneVision is an AI-powered drone detection system built using **YOLO11** and a custom drone dataset.

The system can detect drones in **images and videos** and provides a simple **Python GUI** for running video-based detection.

---

##  Objective

The objective of DroneVision is to develop a computer vision system capable of automatically detecting drones from visual data.

The project uses a custom-trained YOLO model to identify drones and draw bounding boxes around detected objects.



##  Features

-  Drone detection using YOLO11
-  Detection in images
-  Detection in videos
-  Graphical User Interface using Tkinter
-  Video file selection through GUI
-  Bounding boxes around detected drones
-  GPU acceleration using NVIDIA CUDA
-  Custom-trained model



##  How It Works

The system follows the following pipeline:

```text
Input Image / Video
        ↓
     YOLO11
        ↓
Image Processing
        ↓
Drone Detection
        ↓
Bounding Box 
        ↓
Displayed Result
```

## Technology Used :
- Python
- Tkinter
- YOLO
- Open CV
- Pillow

## Project Structure : 
DroneVision/
│
├── src/
│   ├── dashboard.py
│   └── drone_detection.py
│
├── examples/
│   ├── drone_input.jpg
│   └── drone_detection.jpg
│
├── requirements.txt
├── .gitignore
└── README.md


 ## File Description

 # src/dashboard.py

Main GUI application.

It allows the user to:

Select a video
Start drone detection
View the detection results
Stop the video

# src/drone_detection.py

Performs drone detection on an individual image using the trained YOLO model.

# examples/

Contains example images showing the input and the corresponding detection result.

# requirements.txt

Contains the Python libraries required to run the project.

 ## Installation
1. Clone the repository
git clone https://github.com/codernarayanidesh29/DroneVision.git

2 Then enter the project directory:
cd DroneVision

3. Install dependencies
pip install -r requirements.

## Model Setup

The trained model is saved as:

best.pt

The model file is not included in this repository because trained model files can be large.

## Image Detection

 The image detection script can be used to detect drones in an image.

Run:

python src/drone_detection.py

The model processes the input image and displays the detected drone with its bounding box and confidence score.

 ## Video Detection

The project includes a graphical interface for video detection.

Run:
python src/dashboard.py

 # Steps
1. Launch the application.
2. Click SELECT VIDEO.
3. Choose a drone video.
4. Click START DETECTION.
5. The video is processed frame-by-frame.
6. Detected drones are displayed with bounding boxes.
7. Click STOP to stop the detection.

## Examples : 
<img width="612" height="418" alt="drone_test" src="https://github.com/user-attachments/assets/0810b82e-6eb7-43c8-8e34-024ec29231e2" />
<img width="1908" height="972" alt="image" src="https://github.com/user-attachments/assets/502e7c2d-29a2-41a8-a498-4b55d67f52f7" />

## Author
 Narayani Deshpande




