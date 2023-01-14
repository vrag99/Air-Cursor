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
from threading import Thread
import caller_class


#print("it is just a branch ")
tracker = HandTracker()
# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands


# cap = cv2.VideoCapture(0)
# with mp_hands.Hands(
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5) as hands:
    
#   while cap.isOpened():
    
#     success, image = cap.read()
    #privacy.pir(image)



# cap = cv2.VideoCapture(0)
        
# while cap.isOpened():
#     success, image = cap.read()
#     privacy = Thread(target=pir , args=(image, ) , daemon = True)
#     privacy.start()
        
    
#     if not success:
#       print("Ignoring empty camera frame.")
#       continue

caller_class.call_c()    
   
#     image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
   
#     image.flags.writeable = False
#     results = hands.process(image)
#     image_height, image_width, _ = image.shape
#     # Draw the hand annotations on the image.
#     image.flags.writeable = True
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#     condition = GestureRecognition.recognise(image)
#    # handposI= tracker.getLms(image, 9)[1]
#     if(condition == '3-fingers-up_thumb_closed'):
#         print("Scrolling")
#         cv2.destroyAllWindows()
#         Scroll.scroll()
#     elif(condition == '2-fingers-up_thumb_opened'):
#         print("zooming")
#         cv2.destroyAllWindows()
#         zoom.Zoom()
#     elif(condition == 'index-finger-up_thumb_opened'):
#          cv2.destroyAllWindows()
#          CursorControl.cc()
#     elif(condition == 'open-palm' ):
#         cv2.destroyAllWindows()
#         #time.sleep(3)
#         cap = cv2.VideoCapture(0)
        
#         while cap.isOpened():
    
#             success, image = cap.read()
#             image = cv2.flip(image, 1)
#             contri = GestureRecognition.recognise(image)
#             if(contri == 'fist'):
#                 pyautogui.hotkey('win','d')
#                 break        
#             else:
#              volumeHandController.vhc()









        
        
#     if results.multi_hand_landmarks:
#       for hand_landmarks in results.multi_hand_landmarks:
       
     
#         mp_drawing.draw_landmarks(
#             image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#     cv2.imshow('MediaPipe Hands', image)
#     if cv2.waitKey(1) & 0xFF == 'q':
#      break
#cap.release()


  