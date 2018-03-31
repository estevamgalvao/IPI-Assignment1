import cv2
import numpy as np

#VARIÁVEIS:
filaQ = []
tabela_de_pixels = []
listVizinhos = [0, 0, 0, 0, 0, 0, 0, 0]
marcadorL = 0

teste2 = cv2.imread("spots.tif")#leio a imagem original
height, width, channels = teste2.shape

#crio um array em branco com 2 linhas e 2 colunas a mais que a foto original
teste = np.full((height+2,width+2,3), 255)
height, width, channels = teste.shape


conteudo = teste2[0:512, 0:512]#copio o conteudo todo_da foto original
teste[1:513, 1:513] = conteudo#colo exatamente no meio do array em branco


cv2.imwrite("spots2N.tif", teste)
cv2.imshow("spots.tif", teste)
cv2.waitKey(0)

for j in range(1, height): #linhas -> anda pelo eixo Y
    for i in range(1, width): #colunas -> anda pelo eixo X
        if(teste[j, i, 0] == 0):

            pixelP = [marcadorL,j,i]
            teste[j, i, 0] = marcadorL + 15 #mudo a cor do pixel, "marcando ele", evitando que ele seja verificado novamente e entre em loop infinito
            teste[j, i, 1] = marcadorL + 15
            teste[j, i, 2] = marcadorL + 15
            filaQ.append(pixelP)

            while(len(filaQ)!=0):
                pixelQ = filaQ.pop(0)

                listVizinhos[0] = [pixelQ[2] - 1, pixelQ[1] + 1]
                listVizinhos[1] = [pixelQ[2], pixelQ[1] + 1]
                listVizinhos[2] = [pixelQ[2] + 1, pixelQ[1] + 1]
                listVizinhos[3] = [pixelQ[2] - 1, pixelQ[1]]
                listVizinhos[4] = [pixelQ[2] + 1, pixelQ[1]]
                listVizinhos[5] = [pixelQ[2] - 1, pixelQ[1] - 1]
                listVizinhos[6] = [pixelQ[2], pixelQ[1] - 1]
                listVizinhos[7] = [pixelQ[2] + 1, pixelQ[1] - 1]

                # [5,6,7]
                # [3,x,4]
                # [0,1,2]

                for elemento in listVizinhos:
                    if(teste[elemento[1],elemento[0],0]==0):

                        pixelAUX = [marcadorL, elemento[1], elemento[0]]
                        teste[elemento[1], elemento[0], 0] = marcadorL + 15 #mesmo procedimento de marcar, porém agora dentro do loop dos pixels vizinhos
                        filaQ.append(pixelAUX)

            marcadorL += 1 #incremento o marcador para saber quantos elementos o programa encontrou

print(marcadorL)
