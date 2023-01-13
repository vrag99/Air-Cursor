# TRASH CODE NOT IMPORTABLE
import cv2
from HandTrackerModule import HandTracker
import pyautogui
import mediapipe

pyautogui.FAILSAFE=False

vid = cv2.VideoCapture(0)
tracker = HandTracker()

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
sensitivity=1.5

l=[]
while True:
    success, img = vid.read()
    img = cv2.flip(img,1)
    indexFingerTip = tracker.getLms(img, 8)
    middleFingerTip = tracker.getLms(img,12)
    img = tracker.findHands(img)
    
    cv2.imshow('frame',img)
    h,w,c = img.shape
    if indexFingerTip != None and middleFingerTip!=None:
        move_x = SCREEN_WIDTH//w*indexFingerTip[0]*sensitivity
        move_y = SCREEN_HEIGHT//h*indexFingerTip[1]*sensitivity

        x1,y1 = indexFingerTip
        x2,y2 = middleFingerTip
        l.append(y1)
        cv2.line(img,(x1,y1),(x2,y2),(255,255,0), 3)
        distance = ((x1-x2)**2+(y1-y2)**2)**0.5
        if len(l)>=2:
            if distance<25 and y1-l[1]>0:
                pyautogui.scroll(100,None,None)
            elif distance<25 and y1-l[1]<0 : 
                pyautogui.scroll(-100,None,None)
            else:
                pyautogui.moveTo(move_x,move_y)
        if len(l)==8:
            l.clear()
    if cv2.waitKey(1) == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()