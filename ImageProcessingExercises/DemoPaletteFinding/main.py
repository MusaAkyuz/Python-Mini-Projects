import cv2
import numpy as np
import time

image = cv2.imread("DemoPaletteFinding\\image.jpg")
image2 = cv2.imread("DemoPaletteFinding\\image2.jpg")
image3 = cv2.imread("DemoPaletteFinding\\image3.jpg")
image4 = cv2.imread("DemoPaletteFinding\\image4.webp")
image5 = cv2.imread("DemoPaletteFinding\\image5.jpg")
image6 = cv2.imread("DemoPaletteFinding\\image6.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
gray4 = cv2.cvtColor(image4, cv2.COLOR_BGR2GRAY)
gray5 = cv2.cvtColor(image5, cv2.COLOR_BGR2GRAY)
gray6 = cv2.cvtColor(image6, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (1,1), 0)
blur2 = cv2.GaussianBlur(gray2, (1,1), 0)
blur3 = cv2.GaussianBlur(gray3, (9,9), 0)
blur4 = cv2.GaussianBlur(gray4, (9,9), 0)
blur5 = cv2.GaussianBlur(gray5, (9,9), 0)
blur6 = cv2.GaussianBlur(gray6, (1,1), 0)

cv2.imshow("", blur)
cv2.waitKey()
cv2.imshow("", blur2)
cv2.waitKey()
cv2.imshow("", blur3)
cv2.waitKey()
cv2.imshow("", blur4)
cv2.waitKey()
cv2.imshow("", blur5)
cv2.waitKey()
cv2.imshow("", blur6)
cv2.waitKey()

thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)
thresh2 = cv2.adaptiveThreshold(blur2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)
thresh3 = cv2.adaptiveThreshold(blur3,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)
thresh4 = cv2.adaptiveThreshold(blur4,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)
thresh5 = cv2.adaptiveThreshold(blur5,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)
thresh6 = cv2.adaptiveThreshold(blur6,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)

(T, th1) = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)
(T, th2) = cv2.threshold(blur2, 200, 255, cv2.THRESH_BINARY)
(T, th3) = cv2.threshold(blur3, 200, 255, cv2.THRESH_BINARY)
(T, th4) = cv2.threshold(blur4, 200, 255, cv2.THRESH_BINARY)
(T, th5) = cv2.threshold(blur5, 200, 255, cv2.THRESH_BINARY)
(T, th6) = cv2.threshold(blur6, 200, 255, cv2.THRESH_BINARY)

cv2.imwrite("DemoPaletteFinding\\imageout.jpg", th1)
cv2.imwrite("DemoPaletteFinding\\image2out.jpg", th2)
cv2.imwrite("DemoPaletteFinding\\image3out.jpg", th3)
cv2.imwrite("DemoPaletteFinding\\image4out.jpg", th4)
cv2.imwrite("DemoPaletteFinding\\image5out.jpg", th5)
cv2.imwrite("DemoPaletteFinding\\image6out.jpg", th6)