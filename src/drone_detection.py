# ---------- DRONE DETECTION ----------#
from ultralytics import YOLO
# Load the model 
model = YOLO("runs/detect/train-2/weights/best.pt")

# detect drone in image
results = model("drone_test.jpg", conf = 0.25)

for result in results:
    result.show()