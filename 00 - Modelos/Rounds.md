test_cases = int(input())
list = []

for i in range(test_cases):
    x = input()
    x_split = x.split()
    int_x = [int(num) for num in x_split]
    list.append(int_x)
