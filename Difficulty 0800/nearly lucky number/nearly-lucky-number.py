number = int(input())
number_str = str(number)
lista_number = [int(digit) for digit in number_str]

lucky = 0

for digit in lista_number:
    if digit == 4 or digit == 7:
        lucky += 1

if lucky == 4 or lucky == 7:
    print("YES")
else:
    print("NO")
