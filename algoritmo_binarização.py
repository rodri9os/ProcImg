import cv2
import numpy as np

img = cv2.imread('training_set/dogs/dog.14.jpg',0)

tam = img.shape

lin = tam[0]
col = tam[1]
# LINHA E COLUNAS

threshold = int(input('Número do threshold: '))

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

# juntando as imagens
asDuas = np.hstack((img,img_nova))

cv2.imshow('as duas',asDuas)

cv2.imshow('img Original',img)
cv2.imshow('Binarizaçao',img_nova)

k = cv2.waitKey(0)


## Em forma de função
## Passar a imagem ao chama-la
def binarizazao(img):
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