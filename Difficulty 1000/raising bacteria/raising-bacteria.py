num_bacterias = int(input())

bacteria_count = bin(num_bacterias).count('1')

print(bacteria_count)

'''
No contexto do problema, você está tentando alcançar um determinado número de bactérias na caixa, representado por
'num_bacterias'. A ideia é que, a cada noite, todas as bactérias na caixa se dividem em duas. Portanto, para obter
exatamente 'num_bacterias' bactérias na caixa, você precisa adicionar bactérias de forma que, após uma série de divisões 
noturnas, o número total de bactérias seja igual a 'num_bacterias'. Para fazer isso, você precisa colocar um número
de bactérias na caixa igual ao número de bits definidos na representação binária de 'num_bacterias'.
'''
