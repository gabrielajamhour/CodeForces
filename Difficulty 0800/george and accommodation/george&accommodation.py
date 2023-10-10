quartos = int(input())
info_list = []

for i in range(quartos):
    info = input()
    infos = info.split()
    info_list.append(infos)

disponibilidade = 0
for x in range(quartos):
    if int(info_list[x][0]) <= int(info_list[x][1]) - 2:
        disponibilidade += 1
    else:
        False

print(disponibilidade)
