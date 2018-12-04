import cv2
from matplotlib import pyplot as plt
import numpy

'''
Histograma de uma imagem
'''

img = cv2.imread('training_set/dogs/dog.14.jpg', 0)

cv2.imshow("test",img)

hist1 = cv2.calcHist([img],[0],None,[256],[0,256])

plt.plot(hist1)
plt.show()

plt.figure()
thrs, dst  = cv2.threshold(img, 110, 256, cv2.THRESH_TRUNC)

hist2 = cv2.calcHist([img],[0],None,[256],[0,256])
plt.imshow(dst,'gray')
plt.show()
