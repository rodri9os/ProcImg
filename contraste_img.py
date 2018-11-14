import cv2
import numpy as np
from matplotlib import pyplot as plt

#img_ori = cv2.imread('training_set/dogs/dog.16.jpg',1)
img = cv2.imread('training_set/dogs/dog.16.jpg',0)
"""
hist, bins = np.histogram(img.flatten(), 256, [0, 256])

#cdf = hist.cumsum()
#cdf_normalized = cdf * hist.max() / cdf.max()

#plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
#plt.legend(('cdf', 'histogram'), loc='upper left')
plt.legend(('histogram'), loc='upper left')
plt.show()
"""


# contraste da img 
equ = cv2.equalizeHist(img)

# juntando as imagens
res = np.hstack((img, equ))

cv2.imshow('as duas img', res)
k = cv2.waitKey(0)
