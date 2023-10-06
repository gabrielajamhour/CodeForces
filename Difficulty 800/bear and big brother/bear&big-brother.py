'''
Peso Limak = a
Peso Bob = b

A cada ano:
    Limak * 3
    Bob * 2

# Quantidade de anos = x    

a * 3^x > b * 2^x 
log (a * 3^x) > log(b * 2^x)
log(a) + log(3^x) > log(b) + log(2^x)
log(a) + x * log(3) > log(b) + x * log(2)
x * log(3) - x * log(2) > log(b) - log(a)
x * (log(3) - log(2)) > log(b/a)
x > (log(b/a)) / (log(3) - log(2))
'''

import math

pesos = str(input())
pesos_separados = pesos.split()
a = int(pesos_separados[0])
b = int(pesos_separados[1])

x = math.log10(a/b) / (math.log10(3) - math.log10(2)) # O número printado não pode ser igual à conta, mas sim maior
x = abs(x)
quantidade_anos = round(x)

if quantidade_anos < x:
    print(quantidade_anos+1)
elif quantidade_anos > x:
    print(quantidade_anos)
else:
    print(1)
