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

    img_nova = np.array(img_nova, np.uint8)

    #cv2.imwrite('img_nova.jpg', img_nova)

    #img_nova = cv2.imread('img_nova.jpg')

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
    
def vizinho (img_bi,i,j):
    
    
    vizinho = {}
    
    tam = img_bi.shape

    lin = tam[0]
    col = tam[1]


    if i == 0 and j == 0:
        vizinho[1] = None
        vizinho[2] = None
        vizinho[3] = None
        vizinho[4] = None
        vizinho[5] = img_bi[i,j+1]
        vizinho[6] = None
        vizinho[7] = img_bi[i+1,j]
        vizinho[8] = img_bi[i+1,j+1]

    elif i == 0 and j == col:
        vizinho[1] = None
        vizinho[2] = None
        vizinho[3] = None
        vizinho[4] = img_bi[i,j-1]
        vizinho[5] = None
        vizinho[6] = img_bi[i+1,j-1]
        vizinho[7] = img_bi[i+1,j]
        vizinho[8] = None


    if i == 0 :
        vizinho[1] = None
        vizinho[2] = None
        vizinho[3] = None
        vizinho[4] = img_bi[i,j-1]
        vizinho[5] = img_bi[i,j+1]
        vizinho[6] = img_bi[i+1,j-1]
        vizinho[7] = img_bi[i+1,j]
        vizinho[8] = img_bi[i+1,j+1]

       
    elif i == lin and j == 0 :
        vizinho[1] = None
        vizinho[2] = img_bi[i-1,j]
        vizinho[3] = img_bi[i-1,j+1]
        vizinho[4] = None
        vizinho[5] = img_bi[i,j+1]
        vizinho[6] = None
        vizinho[7] = None
        vizinho[8] = None

        
    elif i == lin and j == col:
        vizinho[1] = img_bi[i-1,j-1]
        vizinho[2] = img_bi[i-1,j]
        vizinho[3] = None
        vizinho[4] = img_bi[i,j-1]
        vizinho[5] = None
        vizinho[6] = None
        vizinho[7] = None
        vizinho[8] = None

    elif j == col:
        vizinho[1] = img_bi[i-1,j-1]
        vizinho[2] = img_bi[i-1,j]
        vizinho[3] = img_bi[i-1,j+1]
        vizinho[4] = img_bi[i,j-1]
        vizinho[5] = img_bi[i,j+1]
        vizinho[6] = None
        vizinho[7] = None
        vizinho[8] = None
        
    else:    
        vizinho[1] = img_bi[i-1,j-1]
        vizinho[2] = img_bi[i-1,j]
        vizinho[3] = img_bi[i-1,j+1]
        vizinho[4] = img_bi[i,j-1]
        vizinho[5] = img_bi[i,j+1]
        vizinho[6] = img_bi[i+1,j-1]
        vizinho[7] = img_bi[i+1,j]
        vizinho[8] = img_bi[i+1,j+1]
        
    return vizinho
    
    
    

