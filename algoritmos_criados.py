import cv2
import numpy as np

def binarizacao(img, threshold):

    tam = img.shape

    lin = tam[0]
    col = tam[1]

    img_nova = []

    for i in range(lin):
        linha = []
        for j in range(col):
            if threshold >= img[i][j]:
                linha.append(0)
            else:
                linha.append(255)
        img_nova.append(linha)

    img_nova = np.array(img_nova)

    cv2.imwrite('img_nova.jpg', img_nova)

    img_nova = cv2.imread('img_nova.jpg', 0)

    return img_nova


def threshold (img,threshold):
    tam = img.shape

    lin = tam[0]
    col = tam[1]

    img_nova = []

    for i in range(lin):
        linha = []
        for j in range(col):
            if threshold >= img[i][j]:
                linha.append(img[i][j])
            else:
                linha.append(255)
        img_nova.append(linha)

    img_nova = np.array(img_nova)

    cv2.imwrite('img_nova.jpg', img_nova)

    img_nova = cv2.imread('img_nova.jpg', 0)
