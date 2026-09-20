import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
from ultralytics import YOLO


# --------------------------------
# Load your trained YOLO model
# --------------------------------

model = YOLO("runs/detect/train-2/weights/best.pt")


# --------------------------------
# Create main window
# --------------------------------

window = tk.Tk()

window.title("DroneVision - AI Drone Detection")
window.geometry("1000x650")
window.configure(bg="#101820")


# --------------------------------
# Variables
# --------------------------------

video_path = None
cap = None
running = False


# --------------------------------
# Title
# --------------------------------

title = tk.Label(
    window,
    text="DRONEVISION",
    font=("Arial", 28, "bold"),
    fg="white",
    bg="#101820"
)

title.pack(pady=(25, 5))


subtitle = tk.Label(
    window,
    text="AI Drone Detection System",
    font=("Arial", 14),
    fg="lightgray",
    bg="#101820"
)

subtitle.pack()


# --------------------------------
# Video display area
# --------------------------------

video_frame = tk.Frame(
    window,
    width=800,
    height=400,
    bg="#1b2838"
)

video_frame.pack(pady=25)

video_frame.pack_propagate(False)


video_label = tk.Label(
    video_frame,
    text="NO VIDEO SELECTED",
    font=("Arial", 22, "bold"),
    fg="gray",
    bg="#1b2838"
)

video_label.pack(expand=True)


# --------------------------------
# Select Video
# --------------------------------

def select_video():

    global video_path

    video_path = filedialog.askopenfilename(
        title="Select Drone Video",
        filetypes=[
            ("Video Files", "*.mp4 *.avi *.mov *.mkv"),
            ("All Files", "*.*")
        ]
    )

    if video_path:

        video_label.config(
            image="",
            text="VIDEO SELECTED\n\n" + video_path.split("/")[-1],
            fg="white"
        )

        video_label.image = None


# --------------------------------
# Start Detection
# --------------------------------

def start_detection():

    global cap
    global running

    if video_path is None:

        video_label.config(
            image="",
            text="Please select a video first!",
            fg="red"
        )

        return

    # Stop previous video if running
    if cap is not None:
        cap.release()

    # Open selected video
    cap = cv2.VideoCapture(video_path)

    running = True

    show_frame()


# --------------------------------
# Process video frame
# --------------------------------

def show_frame():

    global running

    if not running or cap is None:
        return

    ret, frame = cap.read()

    if not ret:

        stop_video()
        return

    # --------------------------------
    # YOLO DETECTION
    # --------------------------------

    results = model(
        frame,
        conf=0.25,
        device=0,
        verbose=False
    )

    # Draw bounding boxes
    annotated_frame = results[0].plot()


    # --------------------------------
    # Convert BGR → RGB
    # --------------------------------

    annotated_frame = cv2.cvtColor(
        annotated_frame,
        cv2.COLOR_BGR2RGB
    )


    # --------------------------------
    # Resize for GUI
    # --------------------------------

    annotated_frame = cv2.resize(
        annotated_frame,
        (780, 380)
    )


    # --------------------------------
    # Convert to Tkinter image
    # --------------------------------

    image = Image.fromarray(annotated_frame)

    photo = ImageTk.PhotoImage(image)


    # --------------------------------
    # Display frame
    # --------------------------------

    video_label.config(
        image=photo,
        text=""
    )

    video_label.image = photo


    # --------------------------------
    # Process next frame
    # --------------------------------

    window.after(
        30,
        show_frame
    )


# --------------------------------
# Stop Video
# --------------------------------

def stop_video():
    global cap

    if cap is not None:
        cap.release()
        cap = None
        video_label.config(
            text="VIDEO STOPPED",
            fg="white"
        )

# --------------------------------
# Buttons
# --------------------------------

select_button = tk.Button(
    window,
    text="📁 SELECT VIDEO",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10,
    command=select_video
)

select_button.pack(pady=(0, 10))


start_button = tk.Button(
    window,
    text="▶ START DETECTION",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10,
    command=start_detection
)

start_button.pack(pady=(0, 10))


stop_button = tk.Button(
    window,
    text="⏹ STOP",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10,
    command=stop_video
)

stop_button.pack()


# --------------------------------
# Run GUI
# --------------------------------

window.mainloop()
