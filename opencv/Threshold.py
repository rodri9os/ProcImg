import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread('training_set/cats/cat.4.jpg',0)
plt.figure(1)
# plt.subplot(2, 1, 1)
plt.imshow(img)
plt.show()


plt.figure(2)
his = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(his, 'b')
plt.xlim([0,256])
plt.show()


