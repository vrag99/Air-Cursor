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
import time

import GestureRecognition

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
conditionInitial = ""   
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    
  while cap.isOpened():
    privacy.pir()
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    image = cv2.flip(image, 1)
    
    condition = GestureRecognition.recognise(image)
    
    if(condition == 'fist' and conditionInitial == 'open-palm' or conditionInitial == 'fist' and condition == 'open-palm'):
      #print("Worked",condition)
      pyautogui.hotkey('win','d')
      conditionInitial = condition  
      time.sleep(1)
    else:
      #print(condition)
      conditionInitial = condition    

    if(conditionInitial == 'fist' and condition == 'open-palm'):
        #print("Worked",condition)
        
        pyautogui.hotkey('win','d') 
        conditionInitial = condition 
        time.sleep(3)
    else:
        #print(condition)
        conditionInitial = condition 

    # cv2.imshow('MediaPipe Hands', image)
    # if cv2.waitKey(1) & 0xFF == 'q':
    #  break
cap.release()
    