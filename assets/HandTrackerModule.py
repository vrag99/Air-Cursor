import cv2
import mediapipe as mp

class HandTracker():
    def __init__(self, staticMode = False, maxHands = 2, complexity = 1, minDetConf = 0.5, minTrackConf = 0.5):
        self.staticMode = staticMode
        self.maxhands = maxHands
        self.complexity = complexity
        self.minDetConf = minDetConf
        self.minTrackConf = minTrackConf
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(staticMode, maxHands, complexity, minDetConf, minTrackConf)
        self.mpDraw = mp.solutions.drawing_utils
    
    
    def findHands(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        detections = self.hands.process(imgRGB)
        
        if detections.multi_hand_landmarks:
            for handLms in detections.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        
        return img
    
    def getLms(self, img, index, details = False):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        detections = self.hands.process(imgRGB)
        
        if detections.multi_hand_landmarks:
            for handLms in detections.multi_hand_landmarks:
                l = handLms.landmark[index]
                h,w,c = img.shape
                if details:
                    x,y = l.x*w, l.y*h
                    return (x,y)
                else:
                    x,y = int(l.x*w), int(l.y*h)
                    return (x,y) 


if __name__ == '__main__':
    
    vid = cv2.VideoCapture(0)
    tracker = HandTracker()
    
    while True:
        success, img = vid.read()
        img = cv2.flip(img, 1)
        lms = tracker.getLms(img, 8)
        print(lms)
        cv2.circle(img, lms, 10, (0,255,255), 5)
        
        img = tracker.findHands(img, draw = False)
        
        cv2.imshow('image', img)
        if cv2.waitKey(1) == ord('q'):
            break 

vid.release()
cv2.destroyAllWindows()
        
            
        