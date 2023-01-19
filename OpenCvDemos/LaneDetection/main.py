"""
The lines on the road that show us where the lanes are act as our constant reference.
We are using canny detector-Hough transform based lane detection.
"""

# input > grayscale > gaussian blur > canny > segment > hough > output
import cv2

# reading colored image
img = cv2.imread("lane.jpg")

# converting colored image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

"""
Creating a Gaussian blur over our grey scale image, 
this is not mandatory as in canny detector will do this step for us.
"""