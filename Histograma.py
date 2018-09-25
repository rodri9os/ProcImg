import cv2
from matplotlib import pyplot as plt
import numpy

img = cv2.imread('training_set/dogs/dog.19.jpg', 0)

cv2.imshow("test",img)

hist = cv2.calcHist([img],[0],None,[256],[0,256])

plt.plot(hist)
plt.show()

plt.figure()
thrs, dst  = cv2.threshold(img, 100, 255, cv2.THRESH_TRUNC)
plt.imshow(dst,'gray')
plt.show()




#k = cv2.waitKey(0)


#plt.figure()
#plt.imshow(img)
#plt.show()

#plt.plot(img)
#plt.imshow(img)

