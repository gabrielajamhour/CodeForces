lista = []

for _ in range(3):
    num = int(input())
    lista.append(num)

lista.sort()

a = lista[0]
b = lista[1]
c = lista[2]

way1 = (a + b) * c
way2 = a + b + c
way3 = a * b * c

maior = max(way1, way2, way3)

print(maior)
