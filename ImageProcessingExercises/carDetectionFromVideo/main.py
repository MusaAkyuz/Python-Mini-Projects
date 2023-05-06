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

    #cv2.imshow('video2', frames)
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()