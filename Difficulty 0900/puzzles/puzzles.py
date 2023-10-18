students, puzzles = map(int, input().split())
# Sem a função map(), seria impressa uma lista de strings

pieces = list(map(int, input().split()))
pieces.sort()

sub_pieces = []

# São criadas sublistas deslocando-se um elemento de cada vez
for i in range(len(pieces) - students + 1):
    x = pieces[i:i + students]
    # Divide uma lista em sublistas de tamanho fixo
    sub_pieces.append(x)

# Agora, é necessário iterar por todas as sublistas e calcular a diferença de cada uma delas
menor_diferenca = float('inf') # Inicializar com um valor infinitamente grande
for y in sub_pieces:
    diferenca = y[-1] - y[0]

    if diferenca < menor_diferenca:
        menor_diferenca = diferenca

print(menor_diferenca)
