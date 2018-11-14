import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.misc import imread

#pegando somente uma das cores da imagem
img = cv2.imread('training_set/cats/cat.19.jpg',0)
plt.figure()
plt.imshow(img)


#teste = img.flatten()
histr = cv2.calcHist([img],[0],None,[256],[0,256])
plt.figure()
plt.plot(histr,'b')
plt.xlim([0,256])
#plt.ylim([400,800])
plt.show()

thrs, dst  = cv2.threshold(img, 100, 256, cv2.THRESH_TRUNC)
plt.imshow(dst,'gray')
plt.show()


#img1 = cv2.imread('Imagens/dog.jpg',0)
#
#histr = cv2.calcHist([img1],[0],None,[256],[0,256])
#plt.plot(histr,'g')
#plt.xlim([0,256])
#plt.show()




#plt.imshow(teste)

#hist,bins = np.histogram(img.flatten(),256,[0,256])
#
#cdf = hist.cumsum()
#cdf_normalized = cdf * hist.max()/ cdf.max()
#
#plt.plot(cdf_normalized, color = 'b')
#plt.hist(img.flatten(),256,[0,256], color = 'r')
#plt.xlim([0,256])
#plt.legend(('cdf','histogram'), loc = 'upper left')
#plt.show()
