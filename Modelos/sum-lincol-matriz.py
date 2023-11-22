n, m = map(int, input().split())
campoSandias = []

for _ in range(n):
    linea = list(map(int, input().split()))
    campoSandias.append(linea)

sumasHorizontales = [sum(linea) for linea in campoSandias]
maxHorizontal = max(sumasHorizontales)

# Para sumasVerticales, transpor a matriz
campoSandias_transposta = zip(*campoSandias)
sumasVerticales = [sum(columna) for columna in campoSandias_transposta]
maxVertical = max(sumasVerticales)

print(max(maxHorizontal, maxVertical))
