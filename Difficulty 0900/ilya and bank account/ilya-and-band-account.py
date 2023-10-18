state = str(input())
lista = [num for num in state]

# Cópias da lista inicial
lista_penultimo = lista[:]
lista_ultimo = lista[:]

if '-' in lista:
    lista_penultimo.pop(-2)
    lista_ultimo.pop(-1)

    lista_penultimo = int(''.join(lista_penultimo))
    lista_ultimo = int(''.join(lista_ultimo))

    print(max(lista_penultimo, lista_ultimo)
else:
    print(state)
