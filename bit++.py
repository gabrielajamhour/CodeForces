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
