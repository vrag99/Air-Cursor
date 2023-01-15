import min
import cv2
import pyautogui
import mediapipe as mp
import GestureRecognition
import Scroll
import CursorControl
import privacy
import volumeHandController
import zoom
from HandTrackerModule import HandTracker

# cap = cv2.VideoCapture(0)
# while True:
#     success, img = cap.read()
#     img = cv2.flip(img,1)
#     condition = GestureRecognition.recognise(img)

#     if(condition == '3-fingers-up_thumb_closed'):
#         print("Scrolling")
#         Scroll.scroll()
#     elif(condition == '2-fingers-up_thumb_opened'):
#         print("zooming")
#         zoom.Zoom()
#     if cv2.waitKey(1) == ord('q'):
#             break

# cap.release()


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue
  
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
   
    image.flags.writeable = False
    results = hands.process(image)
    image_height, image_width, _ = image.shape
    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
       
     
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(1) & 0xFF == 'q':
     break
cap.release()
