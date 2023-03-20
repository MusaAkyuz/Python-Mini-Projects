import cv2
import scipy.ndimage

img = cv2.imread("LoG\\mitsubishi.jpg")
grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

LoG = scipy.ndimage.gaussian_laplace(grayScale, sigma=4, mode="reflect")

cv2.imwrite("LoG\\gray-sigma4-modereflect3.jpg", LoG)