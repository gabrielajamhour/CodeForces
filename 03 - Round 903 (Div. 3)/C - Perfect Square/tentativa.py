testcases = int(input())

for _ in range(testcases):
    num_linhas = int(input())

    matriz = []

    for _ in range(num_linhas):
        linha_string = str(input())
        linha_matriz = [valor for valor in linha_string]
        
        matriz.append(linha_matriz)

    print(matriz)

    matriz_rotacionada = [[0] * num_linhas for _ in range(num_linhas)] # Cria uma matriz n x n preenchida com zeros

    for i in range(num_linhas):
        for j in range(num_linhas):
            matriz_rotacionada[j][(num_linhas-1) - i] = matriz[i][j]

    print(matriz_rotacionada)

    count = 0
    for i in range(num_linhas):
        for j in range(num_linhas):
            if matriz[i][j] != matriz_rotacionada[i][j]:
                count += 1
            
    print(count)
