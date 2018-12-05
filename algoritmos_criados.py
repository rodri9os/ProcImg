import cv2
import numpy as np

def threshold (img,threshold):
    '''
    Fazendo o thresold de uma imagem
    
    A função recebe como parâmetro
    a img e o threshold da imagem

    e retorna a imagem com base naquele threshold
    '''
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

def binarizacao(img, threshold):
    '''
    Algoritmo para binariza a imagem
    transforma-la em preto e branco
    '''

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

    
def vizinho (img,i,j):
    '''
    Função para verificar os vizinhos

    Quando chamada recebe a imagem já binarizada e os pontos "i" e "j"
    '''
    
    
    vizinho = {}
    
    tam = img.shape

    lin = tam[0]
    col = tam[1]


    if i == 0 and j == 0:
        vizinho[str(i-1) +' ' + str(j-1)] = None
        vizinho[str(i-1)+ ' ' +str(j)] = None
        vizinho[str(i-1)+ ' ' +str(j+1)] = None
        vizinho[str(i)+ ' ' +str(j-1)] = None
        vizinho[str(i)+ ' ' +str(j)] = img[i,j]
        vizinho[str(i)+ ' ' +str(j+1)] = img[i,j+1]
        vizinho[str(i+1)+ ' ' +str(j-1)] = None
        vizinho[str(i+1)+ ' ' +str(j)] = img[i+1,j]
        vizinho[str(i+1)+ ' ' +str(j+1)] = img[i+1,j+1]

    elif i == 0 and j == col:
        vizinho[str(i-1) +' ' + str(j-1)] = None
        vizinho[str(i-1)+ ' ' +str(j)] = None
        vizinho[str(i-1)+ ' ' +str(j+1)] = None
        vizinho[str(i)+ ' ' +str(j-1)] = img[i,j-1]
        vizinho[str(i)+ ' ' +str(j)] = img[i,j]
        vizinho[str(i)+ ' ' +str(j+1)] = None
        vizinho[str(i+1)+ ' ' +str(j-1)] = img[i+1,j-1]
        vizinho[str(i+1)+ ' ' +str(j)] = img[i+1,j]
        vizinho[str(i+1)+ ' ' +str(j+1)] = None


    elif i == 0 :
        vizinho[str(i-1) +' ' + str(j-1)] = None
        vizinho[str(i-1)+ ' ' +str(j)] = None
        vizinho[str(i-1)+ ' ' +str(j+1)] = None
        vizinho[str(i)+ ' ' +str(j-1)] = img[i,j-1]
        vizinho[str(i)+ ' ' +str(j)] = img[i,j]
        vizinho[str(i)+ ' ' +str(j+1)] = img[i,j+1]
        vizinho[str(i+1)+ ' ' +str(j-1)] = img[i+1,j-1]
        vizinho[str(i+1)+ ' ' +str(j)] = img[i+1,j]
        vizinho[str(i+1)+ ' ' +str(j+1)] = img[i+1,j+1]

       
    elif i == lin and j == 0 :
        vizinho[str(i-1) +' ' + str(j-1)] = None
        vizinho[str(i-1)+ ' ' +str(j)] = img[i-1,j]
        vizinho[str(i-1)+ ' ' +str(j+1)] = img[i-1,j+1]
        vizinho[str(i)+ ' ' +str(j-1)] = None
        vizinho[str(i)+ ' ' +str(j)] = img[i,j]
        vizinho[str(i)+ ' ' +str(j+1)] = img[i,j+1]
        vizinho[str(i+1)+ ' ' +str(j-1)] = None
        vizinho[str(i+1)+ ' ' +str(j)] = None
        vizinho[str(i+1)+ ' ' +str(j+1)] = None

        
    elif i == lin and j == col:
        vizinho[str(i-1) +' ' + str(j-1)] = img[i-1,j-1]
        vizinho[str(i-1)+ ' ' +str(j)] = img[i-1,j]
        vizinho[str(i-1)+ ' ' +str(j+1)] = None
        vizinho[str(i)+ ' ' +str(j-1)] = img[i,j-1]
        vizinho[str(i)+ ' ' +str(j)] = img[i,j]
        vizinho[str(i)+ ' ' +str(j+1)] = None
        vizinho[str(i+1)+ ' ' +str(j-1)] = None
        vizinho[str(i+1)+ ' ' +str(j)] = None
        vizinho[str(i+1)+ ' ' +str(j+1)] = None

    elif j == col:
        vizinho[str(i-1) +' ' + str(j-1)] = img[i-1,j-1]
        vizinho[str(i-1)+ ' ' +str(j)] = img[i-1,j]
        vizinho[str(i-1)+ ' ' +str(j+1)] = img[i-1,j+1]
        vizinho[str(i)+ ' ' +str(j-1)] = img[i,j-1]
        vizinho[str(i)+ ' ' +str(j)] = img[i,j]
        vizinho[str(i)+ ' ' +str(j+1)] = img[i,j+1]
        vizinho[str(i+1)+ ' ' +str(j-1)] = None
        vizinho[str(i+1)+ ' ' +str(j)] = None
        vizinho[str(i+1)+ ' ' +str(j+1)] = None
        
    else:    
        vizinho[str(i-1) +' ' + str(j-1)] = img[i-1,j-1]
        vizinho[str(i-1)+ ' ' +str(j)] = img[i-1,j]
        vizinho[str(i-1)+ ' ' +str(j+1)] = img[i-1,j+1]
        vizinho[str(i)+ ' ' +str(j-1)] = img[i,j-1]
        vizinho[str(i)+ ' ' +str(j)] = img[i,j]
        vizinho[str(i)+ ' ' +str(j+1)] = img[i,j+1]
        vizinho[str(i+1)+ ' ' +str(j-1)] = img[i+1,j-1]
        vizinho[str(i+1)+ ' ' +str(j)] = img[i+1,j]
        vizinho[str(i+1)+ ' ' +str(j+1)] = img[i+1,j+1]
        
    return vizinho
    
    
def vizinho0(img):
    lista0 ={}
    for i in range(3):
        for j in range(3):
            #if img_bi[i][j] == 0:
            vizinhos = vizinho(img,i,j)
            print(vizinhos[0])
            for v in range(len(vizinhos)):
                print(vizinhos[v])
                print()

            #print(i,j, ' ' ,vizinho)
    return lista0

