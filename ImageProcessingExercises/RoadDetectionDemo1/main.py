import cv2
import numpy as np

image = cv2.imread("RoadDetectionDemo1\\road2.jpg")

# Convert image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define color range for road pixels (yellow and white)
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
lower_white = np.array([0, 0, 200])
upper_white = np.array([180, 30, 255])
lower_gray = np.array([52,52,52])
upper_gray = np.array([170,170,170])

# Create binary mask for road pixels
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask_white = cv2.inRange(hsv, lower_white, upper_white)
mask_gray = cv2.inRange(hsv, lower_gray, upper_gray)
mask_road = cv2.bitwise_or(mask_gray, mask_white)

# Apply morphology operations to remove noise and fill gaps
kernel = np.ones((5,5), np.uint8)
mask_road = cv2.morphologyEx(mask_road, cv2.MORPH_CLOSE, kernel)
mask_road = cv2.morphologyEx(mask_road, cv2.MORPH_OPEN, kernel)

# Apply mask to original image
result = cv2.bitwise_and(image, image, mask=mask_road)

# Display results
cv2.imshow('Original Image', image)
cv2.imshow('Road Mask', mask_road)
cv2.imshow('Road Detection Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()