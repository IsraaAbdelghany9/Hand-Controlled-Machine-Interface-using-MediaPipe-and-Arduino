# Hand-Controlled-Machine-Interface-using-MediaPipe-and-Arduino

This project allows real-time control of external machines (e.g., motors) using hand detection via webcam. It uses **MediaPipe** for hand tracking and **Arduino** for machine control via serial communication.

## 🔧 Features
- Detects left, right, or both hands.
- Sends corresponding signals to an Arduino.
- Can control external devices like motors based on hand gestures.
- Displays visual feedback on screen using OpenCV.

## 📦 Technologies Used
- Python
- OpenCV
- MediaPipe
- Arduino (via Serial Communication)
- Google Protobuf (for classification parsing)

## 🖥️ How It Works
1. The webcam captures video frames.
2. MediaPipe detects hands and classifies them as left or right.
3. Based on detection:
   - `'L'` is sent to Arduino for **left hand**.
   - `'R'` is sent for **right hand**.
   - `'B'` is sent for **both hands**.
   - `'N'` is sent when **no hands** are detected.
4. The Arduino reacts accordingly (e.g., turns on motors or LEDs).

## 📌 Requirements
- Python 3.x
- OpenCV
- MediaPipe
- Google Protobuf
- Arduino with serial port (e.g., `/dev/ttyACM0`)

## 🚀 How to Run
1. Connect your Arduino to the PC.
2. Upload the corresponding Arduino code to listen for `'L'`, `'R'`, `'B'`, `'N'` commands.
3. Run the Python script:

```bash
python proj_1.py
```

## 📋 Summary

This project integrates **MediaPipe** and **Arduino** to provide a real-time hand-controlled interface for managing external devices. The system captures video frames from a webcam and processes them using MediaPipe’s hand tracking model to detect the presence and type of hand gestures. Based on the detected hand (left, right, or both), specific commands are sent to an Arduino board via serial communication to control external devices like motors or LEDs. The project also provides real-time visual feedback on the screen, displaying messages such as “Both Hands,” “Left Hand,” or “Right Hand” depending on the detection. This interface allows for intuitive and interactive human-machine interaction, with potential applications in robotics and automation systems.
