n = int(input())
lista = [int(num) for num in str(n)]

lucky = 0

for digit in lista:
    if digit != 4 and digit != 7:
        lucky = -1

if lucky < 0:
    print("NO")
else:
    print("YES")

'''
Erro: 
input: 7
output: YES
answer: NO

Foi dado o output incorreto pois, de acordo com Petya, o número 7 é um "lucky number", mas ele não está em busca de lucky numbers.
Petya quer números "nearly lucky", ou seja, cuja quantidade de dígitos é um lucky number (4 ou 7).
'''
