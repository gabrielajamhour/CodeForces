test_cases = int(input())
list = []

for i in range(test_cases*2):
    infos = input()
    infos_split = infos.split()
    int_infos = [int(num) for num in infos_split]
    list.append(int_infos)

print(list)

list_eficiencias = [list[i] for i in range(len(list)) if i % 2 != 0]


for linha in list_eficiencias:
    soma = 0
    for elemento in linha:
        soma += elemento
    print(soma*-1)
