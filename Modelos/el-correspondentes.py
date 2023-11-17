lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']

# Usando zip para combinar elementos em posições correspondentes
resultados = list(zip(lista1, lista2))

print(resultados)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

soma_vetorial = [x + y for x, y in zip(lista1, lista2)]

print(soma_vetorial)
