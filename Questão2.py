import cv2
import numpy as np

tabela_de_pixels = {}
marcador = 0
verificador = 0

spots = cv2.imread("spots.tif")#leio a imagem original
height, width, channels = spots.shape
#crio um array em branco com 2 linhas e 2 colunas a mais que a foto original
spotsN = np.full((height+2,width+2,3), 255)
height, width, channels = spotsN.shape

conteudo = spots[0:512, 0:512]#copio o conteudo todo_da foto original
spotsN[1:513, 1:513] = conteudo#colo exatamente no meio do array em branco

cv2.imwrite("spotsN.tif", spotsN)

listMarcador = [0,0,0,0,0,0,0,0]
# [5,6,7]
# [3,x,4]
# [0,1,2]


for j in range(1,height):#linhas
    #print("J: ", j)
    for i in range(1, width):#colunas
        #print("I: ", i)
        #print(spotsN[j,i])
        #print("%dx%d" %(j,i))
        if(spotsN[j,i,0] == 0):

            listMarcador[0] = tabela_de_pixels.get((i - 1, j + 1))
            listMarcador[1] = tabela_de_pixels.get((i, j + 1))
            listMarcador[2] = tabela_de_pixels.get((i + 1, j + 1))
            listMarcador[3] = tabela_de_pixels.get((i - 1, j))
            listMarcador[4] = tabela_de_pixels.get((i + 1, j))
            listMarcador[5] = tabela_de_pixels.get((i - 1, j - 1))
            listMarcador[6] = tabela_de_pixels.get((i, j - 1))
            listMarcador[7] = tabela_de_pixels.get((i + 1, j - 1))
            #input(listMarcador)

            for elemento in listMarcador:
                if type(elemento) == int:
                    if(elemento==1):
                        spotsN[j, i, 0] = 0
                        spotsN[j, i, 1] = 255
                        spotsN[j, i, 2] = 0
                    elif(elemento==2):
                        spotsN[j, i, 0] = 0
                        spotsN[j, i, 1] = 0
                        spotsN[j, i, 2] = 255
                    elif(elemento==3):
                        spotsN[j, i, 0] = 255
                        spotsN[j, i, 1] = 0
                        spotsN[j, i, 2] = 0
                    elif(elemento==4):
                        spotsN[j, i, 0] = 100
                        spotsN[j, i, 1] = 100
                        spotsN[j, i, 2] = 100
                    marcador_aux = elemento
                    verificador = 1
            #print("\nVerificador[%dx%d]: %d" %(j,i, verificador))

            if (verificador == 1):
                tabela_de_pixels[(i, j)] = marcador_aux
            else:
                marcador+=1
                if (marcador == 1):
                    spotsN[j, i, 0] = 0
                    spotsN[j, i, 1] = 255
                    spotsN[j, i, 2] = 0
                elif (marcador == 2):
                    spotsN[j, i, 0] = 0
                    spotsN[j, i, 1] = 0
                    spotsN[j, i, 2] = 255
                elif (marcador == 3):
                    spotsN[j, i, 0] = 255
                    spotsN[j, i, 1] = 0
                    spotsN[j, i, 2] = 0
                elif (marcador == 4):
                    spotsN[j, i, 0] = 100
                    spotsN[j, i, 1] = 100
                    spotsN[j, i, 2] = 100
                tabela_de_pixels[(i,j)] = marcador
                # spotsN[j, i, 0] = 0
                # spotsN[j, i, 1] = 255
                # spotsN[j, i, 2] = 0
            verificador = 0

cv2.imwrite("spotsN_colour.tif", spotsN)
cv2.imshow("spotsN_colour.tif", spotsN)
cv2.waitKey(0)

print(marcador)