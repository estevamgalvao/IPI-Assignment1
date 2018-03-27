import numpy as np
import cv2

from rgb2gray import rgb2grey
from calc_distancia import calc_distancia

imgMars = cv2.imread("Mars.bmp")
height, width, channels = imgMars.shape


#imgRGB 3 canais -> imgGrey ainda com 3 canais.
imgMars_grey = rgb2grey(height, width, imgMars)

#Isso prova que estou preenchendo as 3 matrizes R,G,B com o mesmo valor.
# print(img_mars[i,j,0])
# print(img_mars[i,j,1])
# print(img_mars[i,j,2])

#fazer função que realize a equalização da img

pAtual = [415, 260]
pDestino = [1000, 815]

lista_distancias = calc_distancia(pAtual[0],pAtual[1],pDestino[0],pDestino[1])
lista_distancias.sort()

print(lista_distancias)

#o sort dentro do while tá dando q compara complex com float

# while(pAtual != pDestino):
#     lista_distancias = calc_distancia(pAtual[0],pAtual[1],pDestino[0],pDestino[1])
#     lista_distancias.sort()
#     candidatos = [lista_distancias[0],lista_distancias[1], lista_distancias[2]]
#
#     print(candidatos[0][1])
#     print(candidatos[0][2])
#     print(imgMars_grey[416,261])
#
#     aux = 9999
#     for i in range(3):#[0,3)
#         if(imgMars_grey[candidatos[i][1],candidatos[i][2],0] <= aux): #talvez o <= cause um caminho diferente
#             aux = imgMars_grey[candidatos[i][1],candidatos[i][2],0]
#             pAtual[0] = candidatos[i][1]
#             pAtual[1] = candidatos[i][2]
#
#     print(pAtual[0])
#     imgMars_grey[pAtual[0],pAtual[1],2] = 255
#
# cv2.imshow("Mars.bmp", imgMars_grey)
# cv2.waitKey(0)
