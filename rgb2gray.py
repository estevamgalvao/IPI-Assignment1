def rgb2grey(height, width, img):
    for i in range(height):
        for j in range(width):
            img[i, j] = (0.114 * img[i, j, 0] + #pixel na matriz azul
                         0.587 * img[i, j, 1] + #pixel na matriz verde
                         0.299 * img[i, j, 2])  #pixel na matriz vermelha
    return img