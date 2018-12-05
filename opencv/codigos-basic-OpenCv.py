import numpy as np
import cv2
from matplotlib import pyplot as plt

# ===== Somente CV2 ==========

# == MODOS PARA ABRIR UMA IMAGEM ==
# Carrega uma imagem colorida. Qualquer transparência da imagem será negligenciada. É o sinalizador padrão.
img1 = cv2.imread('imagens/carro.jpeg', 1)
# ou
#img = cv2.imread('imagens/carro.jpeg', cv2.IMREAD_COLOR)

# Ler a imagem na escala cinzenta
img2 = cv2.imread('imagens/carro.jpeg', 0)
# ou
#img = cv2.imread('imagens/carro.jpeg', cv2.IMREAD_GRAYSCALE)

# Carrega imagens como tal, incluindo canal alfa
img3 = cv2.imread('imagens/carro.jpeg', -1)
# ou
#img = cv2.imread('imagens/carro.jpeg', cv2.IMREAD_COLOR)

# Para abrir uma janela com a imagem
# titulo da janela, e a imagem q será aberta
cv2.imshow('colorida', img1)
cv2.imshow('cizenta', img2)
cv2.imshow('não sei', img3)


# Espera uma entrada do teclado
# Seu argumento é o tempo em milissegundos
# Se 0 ele ficará esperando uma entrada
k = cv2.waitKey(0)

if k == 27: #tecla esc
	#fecha todas as janelas
	cv2.destroyAllWindows()

elif k == ord('s'):
	# Para salvar uma imagem
	cv2.imwrite('imagens/test.jpg',img2)
	cv2.destroyAllWindows()


# ===== Usando Matplotlib =====
# Serve para mostrar a imagem em uma janela com opçoes para salvar, ampliar imagem...

'''
img = cv2.imread('imagens/carro.jpeg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

'''