# Cursor-hand-gestures
virtual mouse system that uses a webcam and hand tracking to control the computer cursor using natural hand gestures.
🚀 Features
✋ Hand tracking in real time using MediaPipe
🖱️ Move mouse cursor with index finger
👆 Left click with finger gesture
📜 Smooth scrolling with open hand
✊ Drag & Drop using fist gesture
🧠 Adaptive AI-like smoothing (stable cursor movement)
⚡ Low-latency real-time performance
🎯 Frame-reduced control area for precision
🎮 Gestures
Gesture	Action
☝️ Index finger	Move cursor
☝️ + ✌️ fingers	Left click
🖐️ Open hand	Scroll up/down
✊ Fist	Drag & Drop
🛠️ Tech Stack
Python 🐍
OpenCV 👁️
MediaPipe 🤖
NumPy ➗
PyAutoGUI / Autopy 🖱️
📦 Installation
git clone https://github.com/your-username/ai-virtual-mouse.git
cd ai-virtual-mouse

pip install opencv-python mediapipe numpy pyautogui autopy
▶️ Run
python VirtualMouse.py

Press Q to exit.

🧠 How It Works
Captures video from webcam
Detects hand landmarks using MediaPipe
Converts finger positions into gestures
Maps gestures to mouse actions
Applies smoothing for stable cursor control
🔥 Future Improvements
🤖 AI-based gesture recognition (ML model)
👁️ Eye tracking integration
🔊 Volume and brightness control gestures
🪟 Full OS control (Alt-tab, window management)
📱 Multi-hand support
✨ Pinch-to-zoom gestures
📸 Preview

(Add screenshots or GIFs here of hand tracking in action)

📄 License

This project is open-source and free to use for learning and development.
