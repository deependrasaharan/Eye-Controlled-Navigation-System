# 👁️ Eye-Controlled Navigation System

A powerful hands-free interface that allows users to **control the mouse cursor**, **perform clicks**, **drag-and-drop**, and **trigger gestures** using **eye movements and blinks**, built with OpenCV, MediaPipe, and PyAutoGUI.

---

## 🚀 Features

### ✅ Core Features
- **Cursor Movement**: Track iris position in real-time to control mouse cursor.
- **Left Click via Blink**: Blink your left eye to perform a left click.
- **Right Click via Blink**: Blink your right eye to perform a right click.

### 🔁 Advanced Interactions
- **Drag and Drop**: Close both eyes to hold the click and release to drop.
- **Gesture-Based Commands**: Perform quick eye movement gestures (e.g., look LEFT → RIGHT → LEFT) to open new browser tabs or trigger hotkeys.
- **Calibration Mode**: Calibrate by looking at dots shown in different screen corners before using the system.

### 🤖 ML-Based Blink Detection
- Uses **Eye Aspect Ratio (EAR)** instead of fixed distances for robust and adaptive blink detection.

---

## 🛠️ Requirements

### 🔧 Software
```bash
pip install opencv-python
pip install mediapipe
pip install pyautogui
````

### 💻 Hardware

* A functioning webcam
* Laptop/Desktop capable of real-time video processing

---

## 📦 Installation & Setup

1. **Clone or download the repository.**
2. **Install dependencies:**

   ```bash
   pip install opencv-python mediapipe pyautogui
   ```
3. **Run the script:**

   ```bash
   python main.py
   ```

---

## ⚙️ How It Works

### 📌 Calibration

Before usage, a calibration screen shows 5 dots one-by-one to help align your eye position with screen corners.

### 🧠 Cursor Control

* Uses MediaPipe Face Mesh (landmark 475) to track iris movement.
* Cursor is moved smoothly using `pyautogui.moveTo()` based on gaze.

### 👀 Blink Detection

* EAR is computed from multiple eye landmarks.
* If EAR falls below threshold for a few frames → Blink is detected.
* Different eyes trigger different clicks.

### 🧠 Gesture Recognition

* Eye gesture pattern "LEFT → RIGHT → LEFT" (based on gaze direction) triggers a hotkey: `Ctrl + T` (opens new browser tab).
* Future gestures can be added easily.

### 🖱️ Drag and Drop

* Close both eyes simultaneously to hold a click (`mouseDown`).
* Open both eyes to release (`mouseUp`).

---

## 📺 Usage Instructions

1. Sit comfortably in front of your webcam.
2. Follow the on-screen calibration dots.
3. Move your eyes around to control the cursor.
4. Blink to click, or gesture to trigger actions.
5. Press `q` to quit anytime.

---

## ⚠️ Troubleshooting

| Issue               | Solution                                   |
| ------------------- | ------------------------------------------ |
| Cursor doesn’t move | Ensure proper lighting and face visibility |
| Clicks too frequent | Increase `CLICK_DELAY` or EAR threshold    |
| Drag not releasing  | Try opening eyes wider                     |
| Webcam not detected | Change the index in `cv.VideoCapture(0)`   |

---

## 📚 Technical Stack

* **OpenCV**: For video capture and image processing
* **MediaPipe**: Face mesh for landmark detection (iris + eye tracking)
* **PyAutoGUI**: Mouse automation and hotkey control
* **Tkinter (Optional)**: For future GUI configuration

---

## 🧠 Future Improvements

* GUI configuration for setting EAR thresholds & delays
* Voice command integration
* Cross-platform packaging with installer
* Logging and analytics dashboard for eye activity
* Real-time calibration curve fitting

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* [MediaPipe by Google](https://github.com/google/mediapipe)
* [PyAutoGUI Documentation](https://pyautogui.readthedocs.io/)
* [OpenCV Python](https://docs.opencv.org/)

---

## 🤝 Contributing

Pull requests and feature suggestions are welcome! Please open an issue or submit a PR if you want to contribute.

---
