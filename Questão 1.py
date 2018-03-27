import numpy as np
import cv2
import copy

from rgb2gray import rgb2grey
from calc_distancia import calc_distancia

imgMars = cv2.imread("Mars.bmp")
imgMars_aux = copy.copy(imgMars)
height, width, channels = imgMars.shape

#imgRGB 3 canais -> imgGrey ainda com 3 canais.
imgMars_grey = rgb2grey(height, width, imgMars_aux)

cv2.imshow("Mars.bmp", imgMars_aux)
cv2.imwrite("Mars_grey.bmp", imgMars_grey)
cv2.waitKey(0)

#fazer função que realize a equalização da img

pAtual = [415, 260]
pDestino = [1000, 815]

loucura = 10000
while(pAtual[0] != pDestino[0] and pAtual[1] != pDestino[1]):
    lista_distancias = calc_distancia(pAtual[0],pAtual[1],pDestino[0],pDestino[1])

    lista_distancias.sort()
    candidatos = [lista_distancias[0],lista_distancias[1], lista_distancias[2]]

    #candidatos [[181, 838, 734], [180, 839, 734], [179, 840, 734]
    #lista_distancia [[181, 838, 734], [180, 839, 734], [179, 840, 734], [181, 838, 733], [179, 840, 733], [182, 838, 732], [181, 839, 732], [180, 840, 732]]

    aux = 9999
    for i in range(3):#[0,3)
        if(imgMars_grey[candidatos[i][2],candidatos[i][1],0] <= aux): #talvez o <= cause um caminho diferente
            aux = imgMars_grey[candidatos[i][2],candidatos[i][1],0]
            pAtual[1] = candidatos[i][2]
            pAtual[0] = candidatos[i][1]

    imgMars_grey[pAtual[1],pAtual[0],2] = 255
    imgMars_grey[pAtual[1],pAtual[0],1] = 0
    imgMars_grey[pAtual[1],pAtual[0],0] = 0

    imgMars[pAtual[1],pAtual[0],2] = 0
    imgMars[pAtual[1],pAtual[0],1] = 0
    imgMars[pAtual[1],pAtual[0],0] = 0

cv2.imshow("Mars_grey.bmp", imgMars_grey)
cv2.waitKey(0)

cv2.imwrite("Mars_greyWay.bmp", imgMars_grey)
cv2.imwrite("Mars_Way.bmp", imgMars)
