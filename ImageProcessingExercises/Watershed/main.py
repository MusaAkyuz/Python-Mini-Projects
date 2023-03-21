import cv2
import numpy as np

# image: Input 8-bit 3-channel image.
# markers: Input/output 32-bit single-channel image (map) of markers. It should have the same size as image.
# to use watershed
# watershedOutput = cv2.watershed(image, markers)

# önce resim binary görüntüye dönüştürülür.
img = cv2.imread("Watershed\\money.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite("Watershed\\gray.png", gray)
cv2.imwrite("Watershed\\thresh.png", thresh)

# lekeleri temizlemek için morfology filtreler kullanılır
kernel = np.ones((3,3),np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
cv2.imwrite("Watershed\\closing.png", closing)

# distance transform uygulanır
# bu sayede her bölgenin merkezleri en parlak değere sahip olur.
# bazılarının parlaklıkları az olursa bunlar farklı bölgedir
dist = cv2.distanceTransform(closing, cv2.DIST_L2, 3)
cv2.imwrite("Watershed\\dist.png", dist)

# tekrar thresold yaparak bölgeleri ayırt ederiz
ret, dist1 = cv2.threshold(dist, 0.6*dist.max(), 255, 0)
cv2.imwrite("Watershed\\dist1.png", dist1)

# hepsine label verilir
# marker image oluşturulur
markers = np.zeros(dist.shape, dtype=np.int32)
dist_8u = dist1.astype('uint8')
contours, _ = cv2.findContours(dist_8u, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    cv2.drawContours(markers, contours, i, (i+1), -1)

cv2.imwrite("Watershed\\dist_8u.png", dist_8u)
cv2.imwrite("Watershed\\markers.png", markers)

# karşılaştırma için ufacık bir marker oluştururlur
markerWithCircle = cv2.circle(markers, (15,15), 5, len(contours)+1, -1)
cv2.imwrite("Watershed\\markerWithCircle.png", markerWithCircle)

# artık watershed uygulanabilir
output = cv2.watershed(img, markerWithCircle)
cv2.imwrite("Watershed\\output.png", output)
img[output == -1] = [0,0,255]
cv2.imwrite("Watershed\\result.png", img)





