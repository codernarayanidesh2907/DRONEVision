# -------- Drone detection via video stream -------- #
from ultralytics import YOLO
import cv2

# Load the trained model
model = YOLO("runs/detect/train-2/weights/best.pt")
cap = cv2.VideoCapture("drone_video.mp4") 

while True :
    ret, frame  = cap.read()
    if not ret:
        break
    results = model(frame, conf=0.25, device=0)

    
    annotated_frame = results[0].plot() # bounded boxes and labels on the frame

    # Show the frame
    cv2.imshow("Drone Detection", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release video
cap.release()
cv2.destroyAllWindows()