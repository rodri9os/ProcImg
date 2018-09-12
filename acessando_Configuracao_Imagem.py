import numpy as np
import cv2

img = cv2.imread('imagens/carro.jpeg')

# Forma da imagem
# Linhas, Colunas, Canal
# Se a imagem estiver cinzenta nao mostrara o canal 
# so as linhas e colunas
print(img.shape)

# tamanho da imagem em pixels
print(img.size)

# Tipo de daos da imagem
print(img.dtype)

# ==================
# recortando a imagem e colocando em outro lugar

# a forma tem q ter 60 de diferenca
#[lin : col , lin : col]
#     X     ,    Y
#rec  =  img [ 150 : 210 ,  120 : 160 ]

#cv2.imshow('test', rec)

#print(rec.shape)

# aonde o recorte ira ficar 
#img [ 100 : 134 ,  30 : 70 ]  =  rec

#cv2.imshow('test1', img)

#k = cv2.waitKey(0)
