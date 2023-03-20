import cv2

img = cv2.imread("Rotation\\mitsubishi.jpg")
height, width = img.shape[:2]
center = (width/2, height/2)

rotateMatrix = cv2.getRotationMatrix2D(center=center, angle=12, scale=1)
rotatedImage = cv2.warpAffine(src=img, M=rotateMatrix, dsize=(width, height))

cv2.imwrite("Rotation\\Rmitsubishi.jpg", rotatedImage)