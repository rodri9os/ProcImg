import numpy as np
import cv2

img = cv2.imread('imagens/carro.jpeg' )

px = img [100,195]
print (px)
# resultado
# [ 39  4  60 ]
# azul verde vermelho

# para saber somente o pixel verde
verde = img  [100, 195, 1]
print (verde)
cv2.imshow('original',img)


#pixel
# azul = 0
# verde = 1
# vermelho = 2

#fanzendo uma linha na imagem
img.itemset((100,195,1),255)
img.itemset((100,194,1),255)
img.itemset((100,193,1),255)
img.itemset((100,192,1),255)
img.itemset((100,191,1),255)
img.itemset((101,191,1),255)
img.itemset((102,191,1),255)
img.itemset((103,191,1),255)
img.itemset((104,191,1),255)
img.itemset((105,191,1),255)
img.itemset((106,191,1),255)

#img.item (100,195,1)

cv2.imshow('test',img)
k = cv2.waitKey(0)

