palavra = str(input())
primeira_letra = list(palavra)[0]

a = primeira_letra.capitalize()

palavra = palavra.replace(str(primeira_letra), str(a), 1) # Esse 1 define quantas vezes a substituição será realizada

print(palavra)
