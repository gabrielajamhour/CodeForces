lista = []

for _ in range(3):
    num = int(input())
    lista.append(num)

a = lista[0]
b = lista[1]
c = lista[2]

way1 = a + b + c
way2 = a * b * c
way3 = a + (b * c)
way4 = (a + b) * c
way5 = (a * b) + c
way6 = a * (b + c)

maior = max(way1, way2, way3, way4, way5, way6)

print(maior)
