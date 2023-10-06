palavra = str(input())
primeira_letra = list(palavra)[0] # O comando list() separa as letras de uma string em elementos de uma lista

a = primeira_letra.capitalize()

palavra = palavra.replace(str(primeira_letra), str(a), 1) # Esse 1 define quantas vezes a substituição será realizada

print(palavra)
