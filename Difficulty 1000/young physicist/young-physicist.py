num_vetores = int(input())
coordenadas_list = []

coordenadas_list = [input() for n in range(num_vetores)]

new_list1 = [cord.split() for cord in coordenadas_list]
# Usando o método .split(), os valores ainda são strings

print(new_list1)

soma_coluna = [0] * 3
# Essa variável se comporta como uma lista inicialmente nula com três elementos que armazena as somas de cada coluna

for cord in new_list1:
    for i in range(3):
        soma_coluna[i] += int(cord[i]) # Coloca em soma_coluna a soma de cada coluna em cada elemento

print(soma_coluna)

if all(soma == 0 for soma in soma_coluna):
    print("YES")
else:
    print("NO")

 # A função 'all' é usada para se referir a todos os elementos de uma lista
    # Se não fosse utilizada, seriam verificados elemento por elemento
