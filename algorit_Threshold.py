import cv2
import numpy as np
# from matplotlib import pyplot as plt

img = cv2.imread('training_set/dogs/dog.14.jpg',0)
# plt.figure()
# plt.imshow(img)

tam = img.shape
# print(tam)
lin = tam[0]
col = tam[1]
# LINHA E COLUNAS

# print(type(img))
# print(img[0])

threshold = int(input('Número do threshold: '))


img_nova=[]

for i in range(lin):
    linha=[]
    for j in range(col):
        if threshold >= img[i][j]:
            linha.append(img[i][j])
        else:
            linha.append(255)
    img_nova.append(linha)

img_nova = np.array(img_nova)

# print(type(img_nova))
# print(nova[0])

# print(len(img),len(nova))

cv2.imwrite('img_nova.jpg', img_nova)

img_nova = cv2.imread('img_nova.jpg',0)


cv2.imshow('img Original',img)
cv2.imshow('Threshold',img_nova)

k = cv2.waitKey(0)


"""
import cv2
import numpy as np


img = cv2.imread('training_set/dogs/dog.1.jpg')

lin = len(img)
col = len(img[0])
threshold = 90

lista= []

for i in range(lin):
    if i >= threshold:
        lista.append(i)

print(lista)
#print(img.shape)

#print(len(img[90]))

# for i in tam:
#     print(i)

#499, 327
"""
