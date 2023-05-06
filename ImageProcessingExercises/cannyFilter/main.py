import cv2

img = cv2.imread("cannyFilter\\road3.jpg")

canny = cv2.Canny(img, 127, 180)

cv2.imwrite("cannyFilter\\cannyImagesRoad3.jpg", canny)