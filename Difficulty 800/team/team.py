num_problemas = int(input())
problemastotal = []  # Se cria uma lista para que cada problema possa ser interpretado individualmente

for i in range(num_problemas):
    certeza = input()
    problemastotal.append(certeza)
# Esse "for" cria inputs de acordo com o número de problemas

n = 0
for certeza in problemastotal:
    if certeza == "0 1 1" or certeza == "1 0 1" or certeza == "1 1 0" or certeza == "1 1 1":
        n += 1
# Esse "for" adiciona +1 no valor de n para cada problema que pelo menos duas amigas têm certeza, ou seja, que o número 1 aparece ao menos 2x.

print(n) # O print aparece fora do "for" para que seja printado somente a soma final
