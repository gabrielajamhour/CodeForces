usuario = str(input())
caracteres_unicos = set() # A função set() é usada para criar uma coleção não ordenada de elementos únicos > não permite elementos duplicados

for caractere in usuario:
    caracteres_unicos.add(caractere) # Adiciona apenas elementos únicos > se um elemento já estiver lá, não é adicionado
