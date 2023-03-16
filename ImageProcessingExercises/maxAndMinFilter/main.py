import cv2
import scipy.ndimage

base = cv2.imread("maxAndMinFilter\\base.jpg")
grayScale = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY)

maxFilter = scipy.ndimage.maximum_filter(grayScale, size=5)
minFilter = scipy.ndimage.minimum_filter(grayScale, size=5)

cv2.imwrite("maxAndMinFilter\\maxBase.jpg", maxFilter)
cv2.imwrite("maxAndMinFilter\\minBase.jpg", minFilter)