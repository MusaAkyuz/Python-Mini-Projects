import cv2
import matplotlib.pyplot as plt

img = cv2.imread("plane.jpg")
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img.shape)

plt.imshow(grayscale)
plt.show()