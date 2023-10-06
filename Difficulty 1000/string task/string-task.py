palavra = str(input())
palavra_lower = palavra.lower()
lista_palavra = list(palavra_lower)

vogais = "aeiouy"
lista_final = [letra for letra in lista_palavra if letra not in vogais]

final = ".".join(lista_final)
print("."+final)
