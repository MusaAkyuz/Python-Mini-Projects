import cv2

img = cv2.imread("imageInverse\\mitsubishi.jpg")

reverse = 255 - img

cv2.imwrite("imageInverse\\inverseMitsubishi.jpg", reverse)