numero_divisoes = str(input())
numero_divisoes_list = numero_divisoes.split()
n = int(numero_divisoes_list[0])
k = int(numero_divisoes_list[1])

for i in range(k):
    if n % 10 != 0:
        n -= 1
    elif n % 10 == 0:
        n //= 10

print(n)
