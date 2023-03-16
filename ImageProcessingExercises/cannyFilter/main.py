import cv2

img = cv2.imread("cannyFilter\\mitsubishi.jpg")

canny = cv2.Canny(img, 127, 150)

cv2.imwrite("cannyFilter\\cannyImages4.jpg", canny)