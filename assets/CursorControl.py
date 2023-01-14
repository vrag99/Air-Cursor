import cv2
import mediapipe as mp
import pyautogui 
import time
import GestureRecognition
import Scroll
import zoom
import CursorControl
import privacy
import volumeHandController
from HandTrackerModule import HandTracker


## a trash code version, just controls the pointer and click is enabled (not importable)
pyautogui.FAILSAFE = False
def cc():
    vid = cv2.VideoCapture(0)
    tracker = HandTracker()

    SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
    sensitivity = 1.5

    while True:
        privacy.pir()
        success, img = vid.read()
        img = cv2.flip(img, 1)
        indexFingerTip = tracker.getLms(img, 8)
        thumbTip = tracker.getLms(img, 4)
        clickArea = tracker.getLms(img, 6)
        
        h,w,c = img.shape
        if indexFingerTip != None and thumbTip != None and clickArea != None:
            move_x = SCREEN_WIDTH//w*indexFingerTip[0]*sensitivity
            move_y = SCREEN_HEIGHT//h*indexFingerTip[1]*sensitivity
            pyautogui.moveTo(move_x, move_y)
            
            x1, y1 = thumbTip
            x2, y2 = clickArea
            cv2.line(img, (x1,y1), (x2,y2), (255,255,0), 3)
            distance = ((x1-x2)**2+(y1-y2)**2)**0.5
            if move_y>=h/2:
                if distance <= 33:
                    pyautogui.click(move_x, move_y)
            else:
                if distance <= 28:
                    pyautogui.click(move_x, move_y)
            print(distance)
            
        condition = GestureRecognition.recognise(img)
        cv2.imshow('frame', img)
        if condition !='index-finger-up_thumb_opened' :
            return

    vid.release()
    cv2.destroyAllWindows()
    