import cv2
import mediapipe as mp
import ctypes
count =0
flag=0
def pir(image):
  global count
  global flag
  mp_face_detection = mp.solutions.face_detection
  mp_drawing = mp.solutions.drawing_utils
  
  # For webcam input:
  # cap = cv2.VideoCapture(0)
  with mp_face_detection.FaceDetection(
       model_selection=0, min_detection_confidence=0.5) as face_detection:
  #   while cap.isOpened():
  #     success, image = cap.read()
  #     if not success:
  #       print("Ignoring empty camera frame.")
      
  #       continue

      #image.flags.writeable = False
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      results = face_detection.process(image)

      # Draw the face detection annotations on the image.
      image.flags.writeable = True
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
      if results.detections:
        for detection in results.detections:
          #print(results.detections[0])
        # if (results.detections[0]).z <=
          count+=1
      if count > 1 and flag ==0 :
          #print(count)
          ctypes.windll.user32.LockWorkStation()
          flag+=1
      count =0 
      #mp_drawing.draw_detection(image, results.detections[0])
      
      # Flip the image horizontally for a selfie-view display.
      #cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
    