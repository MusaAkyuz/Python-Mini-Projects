import cv2
import numpy as np
import scipy.ndimage

# opening image
img = cv2.imread("meanFilter\\human.jpg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

meanFilter = np.ones((5,5))/25
convolutionImage = scipy.ndimage.convolve(grayImg, meanFilter)

cv2.imwrite("meanFilter\\meanHuman.jpg", convolutionImage)