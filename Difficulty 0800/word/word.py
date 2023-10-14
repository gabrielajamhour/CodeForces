palavra = str(input())

minusculas = 0
maiusculas = 0

for letra in palavra:
    if letra.isupper():
        maiusculas += 1
    elif letra.islower():
        minusculas += 1

if maiusculas > minusculas:
    print(palavra.upper())
elif minusculas > maiusculas or minusculas == maiusculas:
    print(palavra.lower())
