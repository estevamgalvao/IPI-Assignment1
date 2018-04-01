def negativo_binario(altura, largura, img):

    for j in range(0, altura):
        for i in range(0, largura):
            if(img[j,i,0] == 0):
                img[j, i, 0] = 255
                img[j, i, 1] = 255
                img[j, i, 2] = 255
            else:
                img[j, i, 0] = 0
                img[j, i, 1] = 0
                img[j, i, 2] = 0
