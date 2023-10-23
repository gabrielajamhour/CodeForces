import math

num_bacteria = int(input())

bacteria_count = int(math.ceil(math.log(num_bacteria, 2)))

print(bacteria_count)

'''
O número mínimo de bactérias que você precisa colocar na caixa está relacionado à ideia de divisão exponencial,
onde todas as bactérias se dividem em duas a cada noite. Isso é semelhante a calcular a quantidade de vezes que
você pode dividir 'num_bacteria' por 2 até que o valor chegue à 1. 

Se você pensar sobre isso, isso é essencialmente o logaritmo na base 2 de 'num_bacteria'. O logaritmo na base 2
nos dirá quantas vezes podemos dividir 'num_bacteria' por 2 até chegar a 1. O arredondamento para cima (math.ceil)
é necessário porque você não pode ter uma fração de uma bactéria. 
'''
