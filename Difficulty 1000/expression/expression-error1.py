lista = []

for _ in range(3):
    num = int(input())
    lista.append(num)

lista.sort()

a = lista[0]
b = lista[1]
c = lista[2]

way1 = (a + b) * c
way2 = a + b + c
way3 = a * b * c

maior = max(way1, way2, way3)

print(maior)

'''
Erro: 
input: 
6
7
1
output: 49
answer: 48
> O número printado é o maior valor quando realizada uma operação entre os valores, mas não leva em consideração o que foi solicitado no enunciado.

O problema ocorre porque se está modificando a ordem dos valores a b c. De acordo com o enunciado, devem ser adicionados os sinais de operação "+" e "*"
sem alterar a ordem dos valores. No cálculo realizado, fez-se (6 + 1) * 7 = 49, ou seja, (a + c) * b, o que não é possível sem alterar a ordem dos valores fornecidos.
'''
