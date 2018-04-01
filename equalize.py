def equalize(height, width, img):

    ultimo_valido = 18 # Crio essa variável especificamente para essa imagem, pois verifiquei que o tom mais escuro é de valor 18
    tabela_probabilidades = {} # Crio o dicinário que vai realizar os cálculos pra cada tom
    
    for j in range(height): # Percorro a imagem contando quantos pixels tem em cada tom
        for i in range(width):
            if img[j, i, 0] in tabela_probabilidades:
                tabela_probabilidades[img[j, i, 0]] += 1
            else:
                tabela_probabilidades[img[j, i, 0]] = 1

    for chave in tabela_probabilidades: # Calculo a probabilidade de cada tom na imagem
        tabela_probabilidades[chave] /= height * width

    #print(tabela_probabilidades)
    #print(len(tabela_probabilidades))

    for x in range(19, 256): # Calculo a probabilidade acumudala de cada tom
        if (x in tabela_probabilidades):
            tabela_probabilidades[x] += tabela_probabilidades[ultimo_valido]
            ultimo_valido = x # Crio essa variável pois não há pixels em todos os tons de 18 a 256
    #print(tabela_probabilidades)

    for chave in tabela_probabilidades: # Realizo a equalização e o arredondamento das chaves na tabela
        intAUX = int(tabela_probabilidades[chave] * 255)
        tabela_probabilidades[chave] *= 255

        if (tabela_probabilidades[chave] - intAUX) > 0.5:
            intAUX += 1
        tabela_probabilidades[chave] = intAUX

    #print(tabela_probabilidades)

    for j in range(height): # Percorro a imagem pintando os pixels com os novos tons equalizados
        for i in range(width):
            img[j, i, 0] = tabela_probabilidades.get(img[j, i, 0])
            img[j, i, 1] = tabela_probabilidades.get(img[j, i, 1])
            img[j, i, 2] = tabela_probabilidades.get(img[j, i, 2])