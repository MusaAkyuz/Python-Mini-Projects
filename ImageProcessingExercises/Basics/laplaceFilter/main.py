import cv2
import scipy.ndimage

img = cv2.imread("laplaceFilter\\mitsubishi.jpg")
grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

laplace = scipy.ndimage.laplace(grayScale, mode="reflect")

cv2.imwrite("laplaceFilter\\laplaceResultmit.jpg", laplace)