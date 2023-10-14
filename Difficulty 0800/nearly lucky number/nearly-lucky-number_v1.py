n = int(input())
lista = [int(num) for num in str(n)]

lucky = 0

for digit in lista:
    if digit != 4 and digit != 7:
        lucky = -1

if lucky < 0:
    print("NO")
else:
    print("YES")
