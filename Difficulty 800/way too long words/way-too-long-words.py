num_inputs = int(input())
palavrastotal = [] # Se cria uma lista para que cada palavra possa ser interpretada individualmente

for i in range(num_inputs):
    palavra = input()
    palavrastotal.append(palavra)
# Esse "for" cria inputs de acordo com o número de palavras

for palavra in palavrastotal:
    if len(palavra)>10:  # A palavra, para ser abreviada, deve obrigatoriamente conter mais que 10 caracteres
        print(palavra[0],len(palavra)-2,palavra[-1],sep="")
    else:
        print(palavra)
