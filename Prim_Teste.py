import cv2
import numpy as np
from matplotlib import pyplot as plt

img  =  cv2.imread('/Imagens/dog.jpg' , 0) 
#hist  =  cv2.calcHist ([ img ], [ 0 ], none , [ 256 ], [ 0 , 256 ])
"""
"""

#Usando Mat
#plt.hist(img.ravel(),256,[0,256])
#plt.show()

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
    plt.show()

