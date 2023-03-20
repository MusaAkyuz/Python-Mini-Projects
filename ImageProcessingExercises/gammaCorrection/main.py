
# logaritma kısmı hatalı

import cv2
import matplotlib.pyplot as plt
import numpy as np
# Opening the image.
a = cv2.imread('gammaCorrection\\mitsubishi.jpg')
a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
# gamma is initialized.
gamma = 4
# b is converted to type float.
b1 = a.astype(float)
# Maximum value in b1 is determined.
b3 = np.max(b1)
# b1 is normalized
b2 = b1/b3
# gamma-correction exponent is computed.
b4 = np.array(b3*(b1 / b3) ** gamma)
# gamma-correction is performed.
# c = np.exp(b4)*255.0
# c is converted to type int.
c1 = b4.astype(int)
# Displaying c1
cv2.imwrite("gammaCorrection\\mitsubishiGamma.jpg", c1)
