import cv2
import mediapipe as mp
import pyautogui 
import time
import min
import GestureRecognition
import Scroll
import zoom
import CursorControl
from privacy import pir
import volumeHandController
from HandTrackerModule import HandTracker

def call_c():
    cap = cv2.VideoCapture(0)
        
    while cap.isOpened():
    
        success, image = cap.read()
        image = cv2.flip(image, 1)
        condition = GestureRecognition.recognise(image)
        if(condition == '3-fingers-up_thumb_closed'):
            cv2.destroyAllWindows()
            Scroll.scroll()
        elif(condition == '2-fingers-up_thumb_opened'):
            cv2.destroyAllWindows()
            zoom.Zoom()
        elif(condition == 'index-finger-up_thumb_opened'):
            cv2.destroyAllWindows()
            CursorControl.cc()
        elif(condition == 'open-palm' ):
            cv2.destroyAllWindows()
        #time.sleep(3)
            cap = cv2.VideoCapture(0)
        
            while cap.isOpened():
    
                success, image = cap.read()
                image = cv2.flip(image, 1)
                contri = GestureRecognition.recognise(image)
                if(contri == 'fist'):
                    pyautogui.hotkey('win','d')
                    break        
                else:
                    volumeHandController.vhc()

    cap.release()
