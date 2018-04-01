import cv2
import numpy as np
import copy

from pega_vizinhos import pega_vizinhos
from negativo_binário import negativo_binario


# VARIÁVEIS:
filaQ = []
marcadorL = 1
marcadorN = 1

spots = cv2.imread("spots.tif")# leio a imagem original
height, width, channels = spots.shape

# crio um array em branco com 2 linhas e 2 colunas a mais que a foto original
spotsEdge = np.full((height+2,width+2,3), 255)
height, width, channels = spotsEdge.shape


conteudo = spots[0:512, 0:512]# copio o conteudo todo_da foto original
spotsEdge[1:513, 1:513] = conteudo# colo exatamente no meio do array em branco

spotsAUX = copy.copy(spotsEdge)# copio a imagem com bordas para negativa-la em breve

cv2.imwrite("spots_withEdge.tif", spotsEdge)
# cv2.imshow("spots2N.tif", spotsEdge)
# cv2.waitKey(0)

for j in range(1, height):# linhas -> anda pelo eixo Y, a partir do 1 porque o 0 é apenas um contorno
    for i in range(1, width):# colunas -> anda pelo eixo X, a partir do 1 porque o 0 é apenas um contorno
        if(spotsEdge[j, i, 0] == 0):# percorro a imagem em busca de pixels pertos

            pixelP = [marcadorL,j,i]# ao encontrar um pixel preto, recebo suas cordenadas e atribuo a ele um marcador
            spotsEdge[j, i, 0] = marcadorL * 15# mudo a cor do pixel, "marcando ele", evitando que ele seja verificado novamente e fique no while pra sempre

            filaQ.append(pixelP)# adiciono o pixel e seu marcador a uma lista FIFO

            while(len(filaQ) != 0):# enquanto há pixels na lista, continuo verificando e marcando. Fazendo com que ande pela img pixel preto a pixel preto, até terminar "uma célula"
                pixelQ = filaQ.pop(0)

                # organizo os 8 vizinhos de pixelQ em uma lista
                listVizinhos = pega_vizinhos(pixelQ)
                # organização nas posições da lista comparando com a matriz que anda pela img:
                # [5,6,7]
                # [3,x,4]
                # [0,1,2]

                for elemento in listVizinhos:# verifico se algum vizinho é preto, se for, mudo sua cor e o adiciono na fila pra ter seus vizinhos analisados
                    if(spotsEdge[elemento[1],elemento[0],0]==0):

                        pixelAUX = [marcadorL, elemento[1], elemento[0]]
                        spotsEdge[elemento[1], elemento[0], 0] = marcadorL * 15# mesmo procedimento de marcar mudando a cor
                        filaQ.append(pixelAUX)

            marcadorL += 1# incremento o marcador para saber quantas células o programa encontrou

cv2.imwrite("spots_spotted.tif", spotsEdge)

print("Células totais: ", marcadorL-1)# -1 porque o marcador já inicia com 0, afim de impedir que os primeiros pixels não recebam a marcação pela cor, afinal 0*15 = 0... resultando em um loop infinito

negativo_binario(height, width, spotsAUX)# negativo a imagem para fazer com que os buracos se transformem em novas células. As antigas células viram "background", e assim eu posso aplicar o mesmo algoritmo agora buscando os buracos
cv2.imwrite("spots_negativo.tif", spotsAUX)


#### APLICO O MESMO ALGORITMO PARA A NOVA IMAGEM NEGATIVA
for j in range(1, height):# linhas -> anda pelo eixo Y, a partir do 1 porque o 0 é apenas um contorno
    for i in range(1, width):# colunas -> anda pelo eixo X, a partir do 1 porque o 0 é apenas um contorno
        if(spotsAUX[j, i, 0] == 0):# percorro a imagem em busca de pixels pertos

            pixelP = [marcadorN, j, i]# ao encontrar um pixel preto, recebo suas cordenadas e atribuo a ele um marcador
            spotsAUX[j, i, 0] = marcadorN * 15 # mudo a cor do pixel, "marcando ele", evitando que ele seja verificado novamente e fique no while pra sempre

            filaQ.append(pixelP)# adiciono o pixel e seu marcador a uma lista FIFO

            while(len(filaQ) != 0):# enquanto há pixels na lista, continuo verificando e marcando. Fazendo com que ande pela img pixel preto a pixel preto, até terminar "uma célula"
                pixelQ = filaQ.pop(0)

                # organizo os 8 vizinhos de pixelQ em uma lista
                listVizinhos = pega_vizinhos(pixelQ)
                # organização nas posições da lista comparando com a matriz que anda pela img:
                # [5,6,7]
                # [3,x,4]
                # [0,1,2]

                for elemento in listVizinhos:# verifico se algum vizinho é preto, se for, mudo sua cor e o adiciono na fila pra ter seus vizinhos analisados
                    if(spotsAUX[elemento[1],elemento[0],0]==0):

                        pixelAUX = [marcadorN, elemento[1], elemento[0]]
                        spotsAUX[elemento[1], elemento[0], 0] = marcadorN * 15# mesmo procedimento de marcar mudando a cor
                        filaQ.append(pixelAUX)

            marcadorN += 1# incremento o marcador para saber quantas células o programa encontrou

cv2.imwrite("spotsN_spotted.tif", spotsAUX)
print("Células com buracos: ", marcadorN-1)# -1 porque o marcador já inicia com 0, afim de impedir que os primeiros pixels não recebam a marcação pela cor, afinal 0*15 = 0... resultando em um loop infinito
print("\nForam criadas imagens que mostram a lógica do algoritmo!")
