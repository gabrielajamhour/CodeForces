linha1 = str(input())
linha2 = str(input())
linha3 = str(input())
linha4 = str(input())
linha5 = str(input())

matriz = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]

def linha_input_para_matriz(matriz, linha_input, linha_destino):
    elementos = [int(valor) for valor in linha_input.split()] 
    matriz[linha_destino] = elementos
# Compressão de lista, itera sobre a lista de substrings, converte cada substring em um int e cria uma nova lista com os valores convertidos

linha_input_para_matriz(matriz, linha1, 0)
linha_input_para_matriz(matriz, linha2, 1)
linha_input_para_matriz(matriz, linha3, 2)
linha_input_para_matriz(matriz, linha4, 3)
linha_input_para_matriz(matriz, linha5, 4)

mov = 0
for j in range(5):
    if matriz[0][j]:
        if j == 0 or j == 4:
            mov = 4
        elif j == 1 or j == 3:
            mov = 3
        else:
            mov = 2
    if matriz[1][j]:
        if j == 0 or j == 4:
            mov = 3
        elif j == 1 or j == 3:
            mov = 2
        else:
            mov = 1
    if matriz[3][j]:
        if j == 0 or j == 4:
            mov = 3
        elif j == 1 or j == 3:
            mov = 2
        else:
            mov = 1
    if matriz[4][j]:
        if j == 0 or j == 4:
            mov = 4
        elif j == 1 or j == 3:
            mov = 3
        else:
            mov = 2
    if matriz[2][j]:
        if j == 0 or j == 4:
            mov = 2
        elif j == 1 or j == 3:
            mov = 1
        else:
            mov = 0

print(mov)
