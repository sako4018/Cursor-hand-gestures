🖱️ AI Virtual Mouse

Control your computer using only your hand ✋
Built with Python + Computer Vision + AI-style gesture tracking

✨ Overview

This project turns your webcam into a virtual mouse system.
Using hand tracking, you can move the cursor, click, scroll, and drag without touching your mouse.

It uses MediaPipe landmarks + smart smoothing algorithms for real-time control.

🚀 Features

✔ Real-time hand tracking
✔ Smooth cursor movement (AI-style filtering)
✔ Gesture-based control system
✔ Drag & Drop support
✔ Scroll with hand movement
✔ Low latency performance

🎮 Gestures
☝️ Move Cursor

Use only your index finger to move the mouse.

👆 Click

Bring index + middle finger close together → left click

🖐️ Scroll

Open hand → move up/down to scroll

✊ Drag & Drop

Make a fist ✊ → hold object and move cursor
Release fist → drop

🧠 How it works

Webcam frames →
Hand detection (MediaPipe) →
21 hand landmarks →
Gesture logic →
Mouse actions (Autopy / PyAutoGUI)

🛠️ Tech Stack
Python 🐍
OpenCV 👁️
MediaPipe 🤖
NumPy ➗
PyAutoGUI / Autopy 🖱️
⚙️ Installation
git clone https://github.com/your-username/ai-virtual-mouse.git
cd ai-virtual-mouse

pip install opencv-python mediapipe numpy pyautogui autopy
▶️ Run
python VirtualMouse.py

Press Q to exit.

🔮 Future Improvements
🧠 AI gesture recognition (ML model)
👁️ Eye tracking cursor control
🔊 Volume & brightness gestures
🪟 Full OS control system
✨ Pinch-to-zoom gestures
