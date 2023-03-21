import cv2

car = cv2.imread("otherThreSold\\mitsubishi.jpg")
logo = cv2.imread("otherThreSold\\images.png")

carGray = cv2.cvtColor(car, cv2.COLOR_BGR2GRAY)
logoGray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

retCar,thrCar = cv2.threshold(carGray, 0, 255, cv2.THRESH_BINARY)
retLogo,thrLogo = cv2.threshold(logoGray, 0, 255, cv2.THRESH_TRIANGLE)
retInv, threshInv = cv2.threshold(carGray, 230, 255,cv2.THRESH_BINARY_INV)
thresh = cv2.adaptiveThreshold(carGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)

cv2.imwrite("otherThreSold\\thrCar.jpg", thrCar)
cv2.imwrite("otherThreSold\\thrLogo.jpg", thrLogo)
cv2.imwrite("otherThreSold\\thrInv230.jpg", threshInv)
cv2.imwrite("otherThreSold\\thrresh.jpg", thresh)
