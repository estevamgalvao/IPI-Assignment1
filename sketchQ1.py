import numpy as np
import cv2

menor1 = menor2 = menor3 = 0

img_mars = cv2.imread("Mars.bmp")
height, width, channels = img_mars.shape

print(height)
print(width)

cv2.imshow("Mars.bmp", img_mars)
cv2.waitKey(0)

for i in range(height):
    for j in range(width):
        img_mars[i,j] = (0.114*img_mars[i,j,0] +
                         0.587*img_mars[i,j,1] + 0.299*img_mars[i,j,2])

print(channels)

#print(img_mars[260])

cv2.imshow("Mars.bmp", img_mars)
cv2.waitKey(0)

#atual = [260, 415]
#destino = [815, 1000]
lista_distancias = [0, 0, 0, 0, 0, 0, 0, 0]


for i in range(415,width):
    for j in range(260,height):

        distancia1 = ((1000 - (i - 1)) ** 2 + (815 - (j)) ** 2)**(1/2)
        lista_distancias[0] = [distancia1,i-1,j]
        distancia2 = ((1000 - (i - 1)) ** 2 + (815 - (j + 1)) ** 2)**(1/2)
        lista_distancias[1] = [distancia2,i-1,j+1]
        distancia3 = ((1000 - (i)) ** 2 + (815 - (j + 1)) ** 2)**(1/2)
        lista_distancias[2] = [distancia3,i,j+1]
        distancia4 = ((1000 - (i + 1)) ** 2 + (815 - (j + 1)) ** 2)**(1/2)
        lista_distancias[3] = [distancia4,i+1,j+1]
        distancia5 = ((1000 - (i + 1)) ** 2 + (815 - (j)) ** 2)**(1/2)
        lista_distancias[4] = [distancia5,i+1,j]
        distancia6 = ((1000 - (i + 1)) ** 2 + (815 - (j - 1)) ** 2)**(1/2)
        lista_distancias[5] = [distancia6,i+1,j-1]
        distancia7 = ((1000 - (i)) ** 2 + (815 - (j - 1)) ** 2)**(1/2)
        lista_distancias[6] = [distancia7,i,j-1]
        distancia8 = ((1000 - (i - 1)) ** 2 + (815 - (j - 1)) ** 2)**(1/2)
        lista_distancias[7] = [distancia1,i-1,j-1]

        for k in range(7):#[0,7)    [9,8,4,2,0]
            if lista_distancias[k][0] <= lista_distancias[k+1][0]:
                menor3 = menor2
                menor2 = menor1
                menor1 = lista_distancias[k]

            elif lista_distancias[k+1][0] < lista_distancias[k][0]:
                menor3 = menor2#menor3=8
                menor2 = menor1#menor2=4
                menor1 = lista_distancias[k+1]#menor1=2

        if(img_mars[menor1[1]][menor1[2]] < img_mars[menor2[1]][menor2[2]]
                and img_mars[menor1[1]][menor1[2]] < img_mars[menor3[1]][menor3[2]]):

            prox_pixel = [menor1[1], menor1[2]]

        if(img_mars[menor2[1]][menor2[2]] < img_mars[menor1[1]][menor1[2]]
             and img_mars[menor2[1]][menor2[2]] < img_mars[menor3[1]][menor3[2]]):

            prox_pixel = [menor2[1],menor2[2]]

        elif(img_mars[menor3[1]][menor3[2]] < img_mars[menor2[1]][menor2[2]]
                and img_mars[menor3[1]][menor3[2]] < img_mars[menor1[1]][menor1[2]]):

            prox_pixel = [menor3[1], menor3[2]]

