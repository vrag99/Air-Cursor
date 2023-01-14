# TRASH CODE NOT IMPORTABLE
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
import caller_class
pyautogui.FAILSAFE=False
def scroll():
    vid = cv2.VideoCapture(0)
    tracker = HandTracker()

    SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
    sensitivity=1.5
    def scroll1(img):
        upScrollY = (0, 0.25*SCREEN_HEIGHT)
        downScrollY = (0.25*SCREEN_HEIGHT, 0.5*SCREEN_HEIGHT)
        
        fingerTip = tracker.getLms(img, 8)
        
        x, y = fingerTip
        if y>=upScrollY[0] and y<upScrollY[1]:
            pyautogui.scroll(100,None,None)
        elif y>=downScrollY[0] and y<downScrollY[1]:
            pyautogui.scroll(-100,None,None)

    l=[]
    while True:
        
        success, img = vid.read()
        #privacy.pir(img)
        img = cv2.flip(img,1)
        indexFingerTip = tracker.getLms(img, 8)
        middleFingerTip = tracker.getLms(img,12)
        img = tracker.findHands(img)
        scroll1(img)
        #cv2.imshow('frame',img)
        


        if cv2.waitKey(1) & 0xFF == 'q':
            break
               

    vid.release()
    cv2.destroyAllWindows()
    caller_class.call_c()

        
        # h,w,c = img.shape
        # if indexFingerTip != None and middleFingerTip!=None:
        #     move_x = SCREEN_WIDTH//w*indexFingerTip[0]*sensitivity
        #     move_y = SCREEN_HEIGHT//h*indexFingerTip[1]*sensitivity

        #     x1,y1 = indexFingerTip
        #     x2,y2 = middleFingerTip
        #     l.append(y1)
        #     cv2.line(img,(x1,y1),(x2,y2),(255,255,0), 3)
        #     distance = ((x1-x2)**2+(y1-y2)**2)**0.5
        #     if len(l)>=2:
        #         if distance<25 and y1-l[1]>0:
        #             pyautogui.scroll(100,None,None)
        #         elif distance<25 and y1-l[1]<0 : 
        #             pyautogui.scroll(-100,None,None)
        #         else:
        #             pyautogui.moveTo(move_x,move_y)
        #     if len(l)==8:
        #         l.clear()

    # tracker = HandTracker()
        
    
    
