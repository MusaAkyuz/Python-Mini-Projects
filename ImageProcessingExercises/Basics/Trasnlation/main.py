import cv2
import numpy as np

img = cv2.imread("Trasnlation\\mitsubishi.jpg")
height, width = img.shape[:2]
quarterHeight, quartedWidth = height/4, width/4

translation = np.float32([[1,0, quartedWidth], [0, 1, quarterHeight]])

imgTranslation = cv2.warpAffine(img, translation, (width, height))

cv2.imwrite("Trasnlation\\Tmitsubishi.jpg", imgTranslation)