linha1 = str(input())
linha2 = str(input())
linha3 = str(input())
linha4 = str(input())
linha5 = str(input())

matriz = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
          ]

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
movimentos = [
    [4, 3, 2, 3, 4],
    [3, 2, 1, 2, 3],
    [2, 1, 0, 1, 2],
    [3, 2, 1, 2, 3],
    [4, 3, 2, 3, 4]
]

for i in range(5):
    for j in range(5):
        if matriz[i][j] == 1:
            mov += movimentos[i][j]
print(mov)
