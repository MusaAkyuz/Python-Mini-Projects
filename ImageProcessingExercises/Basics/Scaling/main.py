import cv2
import numpy as np

img = cv2.imread("Scaling\\mitsubishi.jpg")

downWidth = 300
downHeight = 200
downPoints = (downWidth, downWidth)
resizeDown = cv2.resize(src=img, dsize=downPoints, interpolation=cv2.INTER_LINEAR)

upWidth = 600
upHeidht = 400
upPoints = (upWidth, upHeidht)
resizeUp = cv2.resize(src=img, dsize=upPoints, interpolation=cv2.INTER_LINEAR)

cv2.imwrite("Scaling\\resizeDown.jpg", resizeDown)
cv2.imwrite("Scaling\\resizeUp.jpg", resizeUp)