import cv2

img = cv2.imread("plane.jpg")

grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imwrite("grayPlane.jpg", grayScale)