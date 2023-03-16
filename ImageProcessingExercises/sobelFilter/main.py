import cv2
import scipy.ndimage

img = cv2.imread("sobelFilter\\images.png")
grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobel = scipy.ndimage.sobel(grayScale)

cv2.imwrite("sobelFilter\\sobelImages.jpg" ,sobel)