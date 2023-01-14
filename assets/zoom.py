import cv2
import mediapipe as mp
import pyautogui
from HandTrackerModule import HandTracker
import math

pyautogui.FAILSAFE = False

# initializing camera
vid = cv2.VideoCapture(0)
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

tracker = HandTracker()

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
reverse_sensitivity = 5  # tells how much change in distance between fingers for zoom

initial, final = 0, 0

while True:
    success, img = vid.read()
    img = cv2.flip(img, 1)
    h = img.shape[0]

    ThumbTip = tracker.getLms(img, 4)
    IndexFingerTip = tracker.getLms(img, 8)
    tracker.findHands(img)

    if IndexFingerTip != None and ThumbTip != None:
        x1, y1 = ThumbTip[0], ThumbTip[1]
        x2, y2 = IndexFingerTip[0], IndexFingerTip[1]

        length = math.hypot(x1 - x2, y1 - y2)

        # cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

        initial = final
        final = length
    change = (final - initial)

    if change < 0:
        # cv2.putText(img, "decrease", (50, 50),
        #             cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
        if abs(change) >= reverse_sensitivity:
            n = int(abs(change)/reverse_sensitivity)
            for i in range(n):
                pyautogui.hotkey('ctrl', '-')

    elif change > 0:
        # cv2.putText(img, "increase", (50, 50),
        #             cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
        if abs(change) >= reverse_sensitivity:
            n = int(abs(change)/reverse_sensitivity)
            for i in range(n):
                pyautogui.hotkey('ctrl', '=')

    # cv2.imshow("video", img)
    # if cv2.waitKey(1) == ord('q'):
    #     break
