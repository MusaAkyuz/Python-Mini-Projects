import cv2
import scipy.ndimage

img = cv2.imread("medianFilter\\human.jpg")
grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

medianFilter = scipy.ndimage.median_filter(grayScale, size=5)

cv2.imwrite("medianFilter\\medianHuman.jpg", medianFilter)

