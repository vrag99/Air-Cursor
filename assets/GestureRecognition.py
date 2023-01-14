import cv2
import mediapipe as mp
from HandTrackerModule import HandTracker
import time


def recognise(img):
    
    tracker = HandTracker()
    try:
        firstFingerDown = tracker.getLms(img, 6)[1] < tracker.getLms(img, 8)[1]
        secondFingerDown = tracker.getLms(img, 10)[1] < tracker.getLms(img, 12)[1]
        thirdFingerDown = tracker.getLms(img, 14)[1] < tracker.getLms(img, 16)[1]
        fourthFingerDown = tracker.getLms(img, 18)[1] < tracker.getLms(img, 20)[1]
        thumbCovered = tracker.getLms(img, 3)[0] < tracker.getLms(img, 4)[0]
        l =  [firstFingerDown, secondFingerDown, thirdFingerDown, fourthFingerDown, thumbCovered]
        
        if all(l) == True:
            return 'fist'
        elif l[0] == False and all(l[1:]) == True:
            return 'index-finger-up'
        elif all(l[:2]) == False and all(l[2:]) == True:
            return '2-fingers-up'
        elif all(l[:3]) == False and all(l[3:]) == True:
            return '3-fingers-up'
        elif all(l[:4]) == False and all(l[4:]) == True:
            return '4-fingers-up'
        elif all(l) == False:
            return 'open-palm'
        
        
    except Exception:
        return None

    

if __name__ == '__main__':
    vid = cv2.VideoCapture(0)
    
    pTime=cTime=0
    while True:
        success, img = vid.read()
        img = cv2.flip(img, 1)
        result = recognise(img)
        print(result)
        
        # img = tracker.findHands(img)
        
        cv2.imshow('frame', img)
        if cv2.waitKey(1) == ord('q'):
            break
    
    vid.release()
    cv2.destroyAllWindows()