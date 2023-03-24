import cv2
import time 
import numpy as np
video = cv2.VideoCapture("carDetectionFromVideo\\video.avi")

#fena değil
xmlDetector = cv2.CascadeClassifier("carDetectionFromVideo\\cars.xml")

while True:
    ret, frames = video.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    cars = xmlDetector.detectMultiScale(gray, 1.1, 1)
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

    #array = [[244, 4,  24,  24],
#  [ 78, 106, 101, 101],
#  [238 , 39 , 25 , 25],
#  [272  ,25 , 24 , 24],
#  [230 , 64 , 56 , 56]]
    
    #array = np.array(array)
    
    cv2.imwrite("carDetectionFromVideo\\deneme.jpg", array)
    #cv2.imshow('video2', frames)
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()