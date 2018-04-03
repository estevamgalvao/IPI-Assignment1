import numpy as np
import cv2
import copy

from rgb2gray import rgb2grey
from calc_distancia import calc_distancia
from equalize import equalize

num_pixels = 0
esforco_pixels = 0

imgMars = cv2.imread("Mars.bmp") # Leio a imagem alvo
imgMars_aux = copy.copy(imgMars) # Aqui copio uma nova imagem para conseguir alterar seus pixels sem afetar a original, pois sem isso são passados por referência
height, width, channels = imgMars.shape # Consigo as dimensões da imagem

imgMars_grey = rgb2grey(height, width, imgMars_aux) # Converto a imagem para cinza

# cv2.imshow("Mars.bmp", imgMars_aux)
cv2.imwrite("Mars_grey.bmp", imgMars_grey) # Salvo a imagem cinza
equalize(height, width, imgMars_grey) # Equalizo a imagem cinza
cv2.imwrite("Mars_eq.bmp", imgMars_grey) # Salvo a imagem equalizada

pAtual = [415, 260]
pAtual_aux = [415, 260]
pDestino = [1000, 815]


while(pAtual[0] != pDestino[0] or pAtual[1] != pDestino[1]): # Enquanto as coordenadas do Pixel Atual e do Pixel Destino não forem iguais, continuo andando
    num_pixels += 1

    lista_distancias = calc_distancia(pAtual[0],pAtual[1],pDestino[0],pDestino[1]) # Calculo as distâncias dos 8 vizinhos do Pixel Atual até o Pixel Destino

    lista_distancias.sort() # Ordeno a lista da menor distância para a maior
    candidatos = [lista_distancias[0],lista_distancias[1], lista_distancias[2]] # Pego os 3 candidatos a ser o novo Pixel Atual

    aux = 9999
    for i in range(3): # Escolho o pixel mais escuro e transformo ele em novo Pixel Atual
        if(imgMars_grey[candidatos[i][2],candidatos[i][1],0] < aux):
            aux = imgMars_grey[candidatos[i][2],candidatos[i][1],0]
            pAtual[1] = candidatos[i][2]
            pAtual[0] = candidatos[i][1]
    esforco_pixels += aux

    imgMars_grey[pAtual[1],pAtual[0],2] = 255 # Pinto de vermelho a imagem cinza equalizada
    imgMars_grey[pAtual[1],pAtual[0],1] = 0
    imgMars_grey[pAtual[1],pAtual[0],0] = 0

    imgMars[pAtual[1],pAtual[0],2] = 0 # Pinto de preto a imagem original
    imgMars[pAtual[1],pAtual[0],1] = 0
    imgMars[pAtual[1],pAtual[0],0] = 0



cv2.imwrite("Mars_greyWay.bmp", imgMars_grey)
cv2.imwrite("Mars_Way.bmp", imgMars)
cv2.imshow("Mars_Way.bmp", imgMars)
cv2.waitKey(0)

print("Imagens criadas!\nO caminho de (%d;%d) até (%d;%d) foi completado em %d pixels com %d unidades de esforço."
      %(pAtual_aux[0], pAtual_aux[1], pDestino[0], pDestino[1], num_pixels, esforco_pixels))
