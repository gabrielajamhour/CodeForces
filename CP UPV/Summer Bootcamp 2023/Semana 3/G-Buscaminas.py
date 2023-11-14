def contar_adjacentes(matriz, linha, coluna):
    bomba = 0
    n = len(matriz)
    m = len(matriz[0])

    for i in range(-1, 2):
        for j in range(-1, 2):
            nova_linha = linha + i
            nova_coluna = coluna + j

            # Verifica se as novas coordenadas estão dentro dos limites da matriz
            # (pode ser que um possível adjacente não esteja dentro desses limites)
            if 0 <= nova_linha < n and 0 <= nova_coluna < m:
                if matriz[nova_linha][nova_coluna] == "*":
                    bomba += 1

    return bomba

def nova_matriz(matriz):
    n = len(matriz)
    m = len(matriz[0])

    # Matriz para armazenar resultado
    campo_resultado = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            # Verifica apenas os elementos que são "."
            if matriz[i][j] == ".":
                campo_resultado[i][j] = contar_adjacentes(matriz, i, j)

    # Substituir "*" por "F" e "0" por " "
    for i in range(n):
        for j in range(m):
            if matriz[i][j] == "*":
                campo_resultado[i][j] = "F"
            elif campo_resultado[i][j] == 0:
                campo_resultado[i][j] = " "

    return campo_resultado

n, m = map(int, input().split())

campo = []

for _ in range(n):
    linha = str(input())
    campo.append(list(linha))

resultado = nova_matriz(campo)

for linha in resultado:
    print("".join(map(str, linha)))
