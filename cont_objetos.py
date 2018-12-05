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

#vizinho = bn.vizinho(img_bi,0,0)

#print(vizinho)

#i = 356
#j = 66

print(bn.vizinho0(img_bi))

"""
for i in range(3):
    for j in range(3):
        if img_bi[i][j] == 0:
            vizinho = bn.vizinho(img_bi,i,j)
            print(i,j, ' ' ,vizinho)
            print()

"""