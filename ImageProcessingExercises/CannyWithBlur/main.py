import cv2
import numpy as np
import scipy
import matplotlib.pyplot as plot

img = cv2.imread("CannyWithBlur\\road3.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
meanFilter = np.ones((5,5))/25
convolutionImage = scipy.ndimage.convolve(gray, meanFilter)

result = cv2.Canny(convolutionImage, 0, 150)
plot.imshow(result)
plot.show()
