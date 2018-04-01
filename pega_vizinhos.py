def pega_vizinhos(pixel):
    listVizinhos = [0, 0, 0, 0, 0, 0, 0, 0]
    
    listVizinhos[0] = [pixel[2] - 1, pixel[1] + 1]
    listVizinhos[1] = [pixel[2], pixel[1] + 1]
    listVizinhos[2] = [pixel[2] + 1, pixel[1] + 1]
    listVizinhos[3] = [pixel[2] - 1, pixel[1]]
    listVizinhos[4] = [pixel[2] + 1, pixel[1]]
    listVizinhos[5] = [pixel[2] - 1, pixel[1] - 1]
    listVizinhos[6] = [pixel[2], pixel[1] - 1]
    listVizinhos[7] = [pixel[2] + 1, pixel[1] - 1]

    return listVizinhos
