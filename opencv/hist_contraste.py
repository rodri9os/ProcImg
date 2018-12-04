import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
Histograma da imagem em contraste
'''

img = cv2.imread('training_set/dogs/dog.11.jpg', 0)

hist, bins = np.histogram(img.flatten(), 256, [0, 256])


contraste = hist.cumsum()
contraste_normalized = contraste * hist.max() / contraste.max()

plt.plot(contraste_normalized, color='b')
# plt.hist(1000, 256, [0, 256], color='r')
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('contraste', 'histogram'), loc='upper left')

plt.show()
