import cv2

car = cv2.imread("otsusMethod\\mitsubishi.jpg")
logo = cv2.imread("otsusMethod\\images.png")

carGray = cv2.cvtColor(car, cv2.COLOR_BGR2GRAY)
logoGray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

retCar,thrCar = cv2.threshold(carGray, 0, 255, cv2.THRESH_OTSU)
retLogo,thrLogo = cv2.threshold(logoGray, 0, 255, cv2.THRESH_OTSU)

cv2.imwrite("otsusMethod\\thrCar.jpg", thrCar)
cv2.imwrite("otsusMethod\\thrLogo.jpg", thrLogo)