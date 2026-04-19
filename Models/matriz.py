# Cria uma matriz de intersecções preenchida com zeros
intersecoes = [[0 for j in range(vertical)] for i in range(horizontal)]

intersecoes = [[(i * vertical + j + 1) for j in range(vertical)] for i in range(horizontal)]
'''
A fórmula "i * vertical" move-se pelas linhas, garantindo que cada linha tenha uma sequência de números única.
Em seguida, j controla o deslocamento horizontal, permitindo que os números sejam preenchidos de cima para baixo,
movendo-se através das colunas. Adicionando 1 a essa fórmula garante que os números sejam contados a partir de 1 em vez de 0
'''
