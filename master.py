from assets.HandTrackerModule import HandTracker
from assets.GestureRecognition import recognise
import cv2
import mediapipe as mp
import pyautogui
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
from assets.privacy import pir
from threading import Thread
import math

pyautogui.FAILSAFE = False
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
sensitivity=1.5

tracker = HandTracker()

vid = cv2.VideoCapture(0)

gestureList = []

initialZoomLen, finalZoomLen = 0,0
initialVolY, finalVolY = 0, 0
while True:
    success, img = vid.read()
    img = cv2.flip(img, 1)
    
    privacy = Thread(target = pir, daemon=True, args=(img,))
    privacy.start()
    
    gesture = recognise(img)
    gestureList.append(gesture)
    if len(gestureList)>3: gestureList.pop(0)
    
    if gestureList[-1] == 'index-finger-up_thumb_opened':
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
            distance = ((x1-x2)**2+(y1-y2)**2)**0.5
            if move_y>=h/2:
                if distance <= 33:
                    pyautogui.click(move_x, move_y)
            else:
                if distance <= 28:
                    pyautogui.click(move_x, move_y)
                
    if gestureList[-1] == '3-fingers-up_thumb_closed':
        upScrollY = (0, 0.25*SCREEN_HEIGHT)
        downScrollY = (0.25*SCREEN_HEIGHT, 0.5*SCREEN_HEIGHT)
        
        fingerTip = tracker.getLms(img, 8)
        
        x, y = fingerTip
        if y>=upScrollY[0] and y<upScrollY[1]:
            pyautogui.scroll(100,None,None)
        elif y>=downScrollY[0] and y<downScrollY[1]:
            pyautogui.scroll(-100,None,None)
            
    if gestureList[-1] == '2-fingers-up_thumb_opened':
        ThumbTip = tracker.getLms(img, 4)
        IndexFingerTip = tracker.getLms(img, 8)
        
        x1, y1 = ThumbTip[0], ThumbTip[1]
        x2, y2 = IndexFingerTip[0], IndexFingerTip[1]
        length = math.hypot(x1 - x2, y1 - y2)
        
        reverse_sensitivity = 10
        
        initialZoomLen, finalZoomLen = finalZoomLen, length
        change = (finalZoomLen - initialZoomLen)
        
        if change < 0:
            if abs(change) >= reverse_sensitivity:
                n = int(abs(change)/reverse_sensitivity)
                for i in range(n):
                    pyautogui.hotkey('ctrl', '-')
                    
        elif change > 0:
            if abs(change) >= reverse_sensitivity:
                n = int(abs(change)/reverse_sensitivity)
                for i in range(n):
                    pyautogui.hotkey('ctrl', '+')
        
    if gestureList[-1] == 'fist':
        openToClose = False
        for i in gestureList:
            if i == 'open-palm':
                openToClose = True
        if openToClose:
            pyautogui.hotkey('win', 'd')
        else:
            pass
    
    if gestureList[-1] == 'open-palm':
        closeToOpen = False
        for i in gestureList:
            if i == 'fist':
                closeToOpen = True
        if closeToOpen:
            pyautogui.hotkey('win', 'd')
        
        else:
            # The volume functionality couldn't be merged.
            pass
            

    img = tracker.findHands(img)
    
    cv2.imshow('img', img)
    if cv2.waitKey(1) == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()

