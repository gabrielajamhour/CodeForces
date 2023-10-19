number = int(input())

lucky_numbers = [4, 7, 47, 74, 44, 77, 444, 447, 474, 477, 744, 747, 774, 777]

divisivel = False

for i in lucky_numbers:
    if number % i == 0:
        divisivel = True
        break

if divisivel:
    print("YES")
else:
    print("NO")
