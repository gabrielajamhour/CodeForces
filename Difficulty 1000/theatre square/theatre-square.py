import math

dimensoes = str(input()) # Digite n m a
lista_separado = dimensoes.split()
n = int(lista_separado[0]) # Comprimento
m = int(lista_separado[1]) # Altura
a = int(lista_separado[2]) # Dimensões laje

comprimento_laje = n / a
comprimento_laje_arredondado = math.ceil(comprimento_laje)
altura_laje = m / a
altura_laje_arredondado = math.ceil(altura_laje)

numero_lajes = comprimento_laje_arredondado * altura_laje_arredondado

print(numero_lajes)
