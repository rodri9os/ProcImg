#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 14:57:39 2018

@author: rodrigos
"""
#está travando -------------


import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Imagens/dog.jpg')
Z = img.reshape((1,1))

plt.figure()
plt.imshow(img)
plt.figure()
plt.imshow(Z)

# convert to np.float32
#Z = np.float32(Z)
#
## define criteria, number of clusters(K) and apply kmeans()
#criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
#K = 8
#ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
#
## Now convert back into uint8, and make original image
#center = np.uint8(center)
#res = center[label.flatten()]
#res2 = res.reshape((img.shape))
#
#cv2.imshow('res2',res2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()