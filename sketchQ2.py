import cv2
import numpy as np

tabela_de_pixels = {}
marcador = 0
verificador = 0

teste = cv2.imread("teste.tif")
cv2.imshow("teste.tif", teste)
cv2.waitKey(0)

height, width, channels = teste.shape

#print("H: %d\nW: %d\nC: %d\n" %(height,width,channels))

listMarcador = [0,0,0,0,0,0,0,0]
# [5,6,7]
# [3,x,4]
# [0,1,2]


for j in range(1,height):#linhas
    #print("J: ", j)
    for i in range(1, width):#colunas
        #print("I: ", i)
        #print(teste[j,i])
        #print("%dx%d" %(j,i))
        if(teste[j,i,0] == 0):

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
                        teste[j, i, 0] = 0
                        teste[j, i, 1] = 255
                        teste[j, i, 2] = 0
                    elif(elemento==2):
                        teste[j, i, 0] = 0
                        teste[j, i, 1] = 0
                        teste[j, i, 2] = 255
                    elif(elemento==3):
                        teste[j, i, 0] = 255
                        teste[j, i, 1] = 0
                        teste[j, i, 2] = 0
                    elif(elemento==4):
                        teste[j, i, 0] = 100
                        teste[j, i, 1] = 100
                        teste[j, i, 2] = 100
                    marcador_aux = elemento
                    verificador = 1
            #print("\nVerificador[%dx%d]: %d" %(j,i, verificador))

            if (verificador == 1):
                tabela_de_pixels[(i, j)] = marcador_aux
            else:
                marcador+=1
                if (marcador == 1):
                    teste[j, i, 0] = 0
                    teste[j, i, 1] = 255
                    teste[j, i, 2] = 0
                elif (marcador == 2):
                    teste[j, i, 0] = 0
                    teste[j, i, 1] = 0
                    teste[j, i, 2] = 255
                elif (marcador == 3):
                    teste[j, i, 0] = 255
                    teste[j, i, 1] = 0
                    teste[j, i, 2] = 0
                elif (marcador == 4):
                    teste[j, i, 0] = 100
                    teste[j, i, 1] = 100
                    teste[j, i, 2] = 100
                tabela_de_pixels[(i,j)] = marcador
                # teste[j, i, 0] = 0
                # teste[j, i, 1] = 255
                # teste[j, i, 2] = 0
            verificador = 0
print(marcador)
cv2.imwrite("teste_colour.tif", teste)
cv2.imshow("teste_colour.tif", teste)
cv2.waitKey(0)

