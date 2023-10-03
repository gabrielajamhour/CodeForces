""" Enunciado 
Em Bitland, a linguagem de programação Bit++ é peculiar e complicada. 
Ela possui uma única variável, "x", e duas operações: "++" que aumenta o valor de "x" em 1, e "--" que diminui o valor de "x" em 1. 
Um programa Bit++ é uma sequência de instruções que devem ser executadas em ordem.

Input:
> Um inteiro "n" (1 ≤ n ≤ 150) - o número de instruções no programa.
> "n" linhas contendo uma instrução cada. Cada instrução contém uma operação ("++" ou "--") e a variável "x", sem espaços.
Output:
> Um único número inteiro - o valor final de "x" após a execução do programa. """

num_instrucoes = int(input())
instrucoestotal = [] # Se cria uma lista para que cada instrução possa ser interpretada individualmente

for i in range(num_instrucoes):
    operacao = (input())
    instrucoestotal.append(operacao)
# Esse "for" cria inputs de acordo com o número de palavras

x=0
for instrucao in instrucoestotal:
    if '++' in instrucao:
        x += 1
    elif '--' in instrucao:
        x -= 1
        
print(x)
