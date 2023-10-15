test_cases = int(input())
lista = []

for i in range(test_cases):
    # Jeito 1 (passo a passo)
    x = input()
    x_split = x.split()
    int_x = [int(num) for num in x_split]
    lista.append(int_x)

    # Jeito 2 (direto)
        # A função map() é uma função embutida que permite aplicar uma função a todos os elementos de um ou mais iteráveis, como listas

    # Dois números juntos de string para int separadamente
    n, p = map(int, input().split())

    # Vários números juntos de string para int em uma lista 
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
