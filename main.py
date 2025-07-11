# Enhanced Eye-Controlled Navigation System

import cv2 as cv
import mediapipe as mp
import pyautogui
import time
import numpy as np
from tkinter import *
from collections import deque
from statistics import mean

# Configurable Parameters
CLICK_DELAY = 1.0
BLINK_EAR_THRESHOLD = 0.21
EYE_AR_HISTORY = 3
GESTURE_SEQUENCE = ['LEFT', 'RIGHT', 'LEFT']
GESTURE_DELAY = 2  # seconds

# MediaPipe and PyAutoGUI setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
cam = cv.VideoCapture(0)

# Indexes for eyes
LEFT_EYE_INDEXES = [33, 133, 160, 159, 158, 144, 153, 154, 155, 173]
RIGHT_EYE_INDEXES = [362, 263, 387, 386, 385, 373, 380, 381, 382, 362]
LEFT_EYE_BLINK = (159, 145)
RIGHT_EYE_BLINK = (386, 374)

# Gesture detection variables
gesture_buffer = deque(maxlen=20)
gesture_last_time = 0

# Blink detection using Eye Aspect Ratio
def eye_aspect_ratio(landmarks, eye_indexes, frame_w, frame_h):
    points = [(int(landmarks[i].x * frame_w), int(landmarks[i].y * frame_h)) for i in eye_indexes]
    hor_line = np.linalg.norm(np.array(points[0]) - np.array(points[1]))
    ver_line1 = np.linalg.norm(np.array(points[2]) - np.array(points[4]))
    ver_line2 = np.linalg.norm(np.array(points[3]) - np.array(points[5]))
    ear = (ver_line1 + ver_line2) / (2.0 * hor_line)
    return ear

# Calibrate user with dot targets
def calibrate():
    calib_screen = np.zeros((400, 800, 3), dtype=np.uint8)
    points = [(100, 100), (700, 100), (400, 200), (100, 300), (700, 300)]
    for x, y in points:
        calib_screen[:] = 0
        cv.circle(calib_screen, (x, y), 20, (0, 255, 255), -1)
        cv.putText(calib_screen, 'Look at the dot', (250, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv.imshow("Calibration", calib_screen)
        cv.waitKey(1000)
    cv.destroyWindow("Calibration")

# Main loop
last_click_time = 0
left_eye_ear_hist = deque(maxlen=EYE_AR_HISTORY)
right_eye_ear_hist = deque(maxlen=EYE_AR_HISTORY)
drag_mode = False

calibrate()

while True:
    success, frame = cam.read()
    if not success:
        break
    frame = cv.flip(frame, 1)
    frame_h, frame_w, _ = frame.shape
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark
        # Cursor Movement via Iris
        iris = landmarks[475]
        screen_x = screen_w * iris.x
        screen_y = screen_h * iris.y
        pyautogui.moveTo(screen_x, screen_y, duration=0.05)

        # Eye Blink Detection (ML via EAR)
        left_ear = eye_aspect_ratio(landmarks, LEFT_EYE_INDEXES, frame_w, frame_h)
        right_ear = eye_aspect_ratio(landmarks, RIGHT_EYE_INDEXES, frame_w, frame_h)
        left_eye_ear_hist.append(left_ear)
        right_eye_ear_hist.append(right_ear)

        if mean(left_eye_ear_hist) < BLINK_EAR_THRESHOLD:
            if time.time() - last_click_time > CLICK_DELAY:
                pyautogui.click()
                last_click_time = time.time()

        elif mean(right_eye_ear_hist) < BLINK_EAR_THRESHOLD:
            if time.time() - last_click_time > CLICK_DELAY:
                pyautogui.click(button='right')
                last_click_time = time.time()

        # Gesture Detection (e.g., left-right-left look)
        if iris.x < 0.35:
            gesture_buffer.append('LEFT')
        elif iris.x > 0.65:
            gesture_buffer.append('RIGHT')

        if time.time() - gesture_last_time > GESTURE_DELAY:
            if list(gesture_buffer)[-3:] == GESTURE_SEQUENCE:
                pyautogui.hotkey('ctrl', 't')  # Open browser tab
                gesture_last_time = time.time()

        # Drag and Drop by holding both eyes shut
        if mean(left_eye_ear_hist) < 0.15 and mean(right_eye_ear_hist) < 0.15:
            if not drag_mode:
                pyautogui.mouseDown()
                drag_mode = True
        elif drag_mode:
            pyautogui.mouseUp()
            drag_mode = False

    cv.imshow("Enhanced Eye Control", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()
