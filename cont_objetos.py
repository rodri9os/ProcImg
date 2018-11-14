import cv2
import numpy as np
import algoritmo_binarização as bn

img = cv2.imread('training_set/dogs/dog.14.jpg',0)

tam = img.shape

lin = tam[0]
col = tam[1]

img_bi = bn.binarizazao(img) # preto e branco

for i in range(lin):
    for j in range(col):
        print()
        ### Não acabado

