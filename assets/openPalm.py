from HandTrackerModule import HandTracker
from GestureRecognition import recognise
import volumeHandController

import cv2

tracker = HandTracker()
def openPalm():
    vid = cv2.VideoCapture(0)
    l=[]
    while True:
        success, img = vid.read()
        gesture = recognise(img)
        print(gesture)
        cv2.imshow('img',img)
        
        if gesture == 'open-palm':
            x, y = tracker.getLms(img, 9)
            l.append((x,y))
            
            if len(l)>=2:
                if y-l[1][1]!=0:
                    volumeHandController.vhc()
                    
            if len(l) == 8:
                l.clear()
                    
        if gesture!='open-palm':
            break
    vid.release()
    cv2.destroyAllWindows()
            
        # if cv2.waitKey
        
openPalm()