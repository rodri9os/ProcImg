import cv2
import numpy as np
from matplotlib import pyplot as plt

img  =  cv2.imread('training_set/dogs/dog.1.jpg') 
cv2.imshow('img colorida',img)

#separando os canais
canais = cv2.split(img)
color = ('b', 'g', 'r')

plt.figure()
plt.title('Hitograma Colorido')
plt.xlabel('Intesidade')
plt.ylabel('Nº de pixels')

for (canal,cor) in zip(canais,color):
    hist = cv2.calcHist([canal],[0],None,[256],[0,256])
    plt.plot(hist, cor = cor)
    plt.xlim([0,256])

plt.show()

