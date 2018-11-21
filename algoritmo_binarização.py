import cv2
import numpy as np
from matplotlib import pyplot as plt
#from skimage.filters import theshold_mininum

def binarizazao(img ,threshold):

    tam = img.shape

    lin = tam[0]
    col = tam[1]

    img_nova=[]

    for i in range(lin):
        linha=[]
        for j in range(col):
            if threshold >= img[i][j]:
                linha.append(0)
            else:
                linha.append(255)
        img_nova.append(linha)

    img_nova = np.array(img_nova)

    cv2.imwrite('img_nova.jpg', img_nova)

    img_nova = cv2.imread('img_nova.jpg',0)

    return img_nova




img = cv2.imread('training_set/dogs/dog.14.jpg',0)

threshold = int(input('Número do threshold: '))

img_nova = binarizazao(img,threshold)

plt.hist(img.ravel(),bins=256)

plt.axvline(threshold, color = 'r')

cv2.imwrite('img_nova.jpg', img_nova)

img_nova = cv2.imread('img_nova.jpg',0)

# juntando as imagens
asDuas = np.hstack((img,img_nova))

cv2.imshow('as duas',asDuas)

#cv2.imshow('img Original',img)
#cv2.imshow('Binarizaçao',img_nova)

#plt.imshow(histograma,'a')
plt.show()


k = cv2.waitKey(0)


## Em forma de função
## Passar a imagem ao chama-la
""""
tam = img.shape

lin = tam[0]
col = tam[1]
# LINHA E COLUNAS



img_nova=[]

for i in range(lin):
    linha=[]
    for j in range(col):
        if threshold >= img[i][j]:
            linha.append(0)
        else:
            linha.append(255)
    img_nova.append(linha)

img_nova = np.array(img_nova)
"""