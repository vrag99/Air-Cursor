import cv2
import mediapipe as mp
import pyautogui
import math
import numpy as np
from HandTrackerModule import HandTracker

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

pyautogui.FAILSAFE = False

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


#initializing camera
vid = cv2.VideoCapture(0)
wCam , hCam  = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

#initializing volume settings
volumeRange = volume.GetVolumeRange()
volMin = volumeRange[0]
volMax = volumeRange[1]
volume.SetMasterVolumeLevel(-65.25, None)

print(volMin, volMax)

# volume.GetMute()
print(volume.GetMasterVolumeLevel()) 

tracker = HandTracker()

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
sensitivity = 0.40

# l = []
ynew, yold = 0, 0
vol = volMin   #it is taccording to system, ie from(-65.25, 0)

while True:
    success, img = vid.read()
    img = cv2.flip(img, 1)
    h = img.shape[0]
    MiddleFingerMcp = tracker.getLms(img, 9)
    tracker.findHands(img)

    # MiddleFingerMcp = MiddleFingerMcp[1]*sensitivity
    if MiddleFingerMcp != None:

        yold = ynew
        ynew = MiddleFingerMcp[1]
        change = ynew - yold 

        if abs(change) > 3:
            if change < 0:
                print("movin up")
            elif change > 0:
                print("movin down")
            cv2.putText(img, "moving up", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            cv2.putText(img, str(-change), (400, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        print(change)

        if(abs(change) > 10):
            vol_change = np.interp(-change, [-200, 200], [-65, 65])
        else: vol_change = 0


        print("vol change", int(vol_change))
        
        vol = vol + vol_change

        print("vol ", int(vol))
        print("break")
        

        if vol > volMax:
            vol = volMax
        elif vol <= volMin:
            vol = volMin

        volume.SetMasterVolumeLevel(vol, None)

    #showing volume
    volume_bar = np.interp(vol, [volMin, volMax], [0, 250])
   
    # print(volume_bar)
    cv2.rectangle(img, (50, 450), (80, 200), (0, 255, 0), 2)
    cv2.rectangle(img, (50, 450), (80, 450 - int(volume_bar)), (0, 255, 0), cv2.FILLED)

    cv2.imshow("video", img)
    if cv2.waitKey(1) == ord('q'):
            break 
