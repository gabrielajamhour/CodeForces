# Verificar se o elemento sucessor em uma lista é igual ao antecessor e somar 1 à uma variável 
same = 0
for i in range(len(color_stones) - 1):
    if color_stones[i] == color_stones[i + 1]:
        same += 1
