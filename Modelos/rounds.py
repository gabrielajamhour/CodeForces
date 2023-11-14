test_cases = int(input())
lista = []

for _ in range(test_cases):
    # A função map() é uma função embutida que permite aplicar uma função a todos os elementos de um ou mais iteráveis, como por exemplo listas
    # Dois números separados por um espaço de string para int separadamente
    n, p = map(int, input().split())

    # Vários números separados por espaços de string para int em uma lista 
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Vários valores sem separação em uma lista separados
    linha = str(input())
    linha_lista = [valor for valor in linha_string]
    # Ou, para que os valores sejam convertidos para inteiros:
    linha_lista = [int(valor) for valor in linha_string]
    lista.append(linha_lista)



