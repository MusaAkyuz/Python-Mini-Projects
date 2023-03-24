# çalışmıyor

import cv2

image = cv2.imread("TextSWT\\image6.jpg")

rects, draw, chainBBs = cv2.text.detectTextSWT(image, True)
for rect in rects:
    cv2.rectangle(image, rect, (255,0,0), 2)

cv2.imshow("img", image)
cv2.imshow("image", draw)
cv2.waitKey(0)
cv2.destroyAllWindows()