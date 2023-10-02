""" Enunciado
Em um texto, palavras com mais de 10 caracteres são substituídas por abreviações.
A abreviação consiste na primeira e última letra da palavra, entre as quais é escrito o número de letras entre elas.

> Input:
    Um inteiro n (1 ≤ n ≤ 100).
    n palavras compostas por letras minúsculas, com comprimentos entre 1 e 100 caracteres.
> Output:
    n linhas contendo as palavras após a substituição por abreviações, se aplicável. """

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
