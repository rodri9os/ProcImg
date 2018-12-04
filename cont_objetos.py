import cv2
import numpy as np
import algoritmos_criados as bn

img = cv2.imread('training_set/dogs/dog.14.jpg',0)
vizinho = {}

tam = img.shape

lin = tam[0]
col = tam[1]

img_bi = bn.binarizacao(img,114) # preto e branco
#cv2.imshow('Figura',img_bi)

#k = cv2.waitKey(0)

vizinho = bn.vizinho(img_bi,356,66)


i = 356
j = 66


for i in range(lin):
    for j in range(col):
        if img_bi[i,j] == 1: 
            print("i = %d, j = %d" % (i,j))
            break