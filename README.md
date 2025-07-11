# Eye-Controlled Navigation System

A computer vision-based system that allows users to control their computer cursor and perform clicks using eye movements and blinks. This project uses facial landmark detection to track eye position and translate it into mouse movements.

## Features

- **Real-time Eye Tracking**: Uses your webcam to track eye movements in real-time
- **Cursor Control**: Move your computer cursor by looking at different parts of the screen
- **Blink-to-Click**: Perform mouse clicks by blinking your left eye
- **Visual Feedback**: See tracked eye landmarks on the video feed

## Requirements

### Hardware
- Webcam (built-in or external)
- Computer with sufficient processing power for real-time video processing

### Software Dependencies
```bash
pip install opencv-python
pip install mediapipe
pip install pyautogui
```

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install opencv-python mediapipe pyautogui
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## How It Works

### Eye Movement Detection
- Uses MediaPipe's Face Mesh to detect 468 facial landmarks
- Tracks specific landmarks around the iris (landmarks 474-478)
- Maps eye position to screen coordinates proportionally

### Blink Detection
- Monitors the vertical distance between upper and lower eyelid landmarks (145 and 159)
- Triggers a click when the distance falls below a threshold (0.005)
- Includes a 1-second delay after each click to prevent multiple triggers

### Coordinate Mapping
The system maps your eye position within the camera frame to your screen coordinates:
```
screen_x = (screen_width / frame_width) * eye_x
screen_y = (screen_height / frame_height) * eye_y
```

## Usage

1. **Start the Application**: Run `python main.py`
2. **Position Yourself**: Sit comfortably in front of your webcam with good lighting
3. **Calibrate**: Look around the screen to get familiar with the sensitivity
4. **Navigate**: Move your eyes to control the cursor
5. **Click**: Blink your left eye to perform clicks
6. **Exit**: Press 'q' to quit the application

## Visual Indicators

- **Green circles**: Show tracked iris landmarks
- **Yellow circles**: Show left eye landmarks used for blink detection
- **Video feed**: Displays the processed camera input with landmarks

## Configuration

You can adjust the following parameters in the code:

- **Blink sensitivity**: Change the threshold value `0.005` in the blink detection condition
- **Click delay**: Modify `pyautogui.sleep(1)` to change the delay between clicks
- **Landmark visualization**: Adjust circle size and colors for better visibility

## Troubleshooting

### Common Issues

1. **No face detected**: 
   - Ensure good lighting
   - Position your face clearly in the camera frame
   - Check if your webcam is working properly

2. **Cursor too sensitive/not sensitive enough**:
   - Adjust your distance from the camera
   - Modify the coordinate mapping ratios

3. **Accidental clicks**:
   - Increase the blink threshold value
   - Increase the click delay duration

4. **Camera not found**:
   - Check if another application is using the webcam
   - Try changing the camera index in `cv.VideoCapture(0)` to `cv.VideoCapture(1)` or higher

## Technical Details

### Libraries Used
- **OpenCV**: Video capture and image processing
- **MediaPipe**: Face mesh detection and landmark tracking
- **PyAutoGUI**: Mouse control and automation

### Landmark Points
- **Iris tracking**: Landmarks 474-478 (right eye iris)
- **Blink detection**: Landmarks 145 and 159 (left eye upper and lower eyelid)

## Safety Considerations

- **Eye strain**: Take regular breaks when using the system
- **Lighting**: Ensure adequate lighting to reduce eye strain
- **Calibration**: Spend time getting familiar with the system before extended use

## Future Enhancements

- Calibration system for improved accuracy
- Support for both eye tracking
- Gesture recognition for additional controls
- Settings interface for easy configuration
- Multiple click types (right-click, double-click)

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have questions, please check the troubleshooting section or open an issue in the repository.
