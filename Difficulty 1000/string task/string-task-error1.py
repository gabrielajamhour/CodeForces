palavra = str(input())
palavra_lower = palavra.lower()
lista_palavra = list(palavra_lower)

for x in lista_palavra:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" or x == "y":
        lista_palavra.remove(x)

final = ".".join(lista_palavra)
print("."+final)

'''
Erro: 
input: tour
output: .t.u.r
> A vogal "u" foi printada ainda que esteja na condição que deveria haver sido eliminada.

O problema ocorre porque se está modificando a lista lista_palavra enquanto itera sobre ela usando um loop for.
Isso pode causar comportamentos inesperados, como a remoção incorreta de elementos e a saída de caracteres indesejados.
'''

