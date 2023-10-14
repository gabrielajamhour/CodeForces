n = int(input())
n_str = str(n)

lucky = True

digits = len(n_str)
lista = [int(digit) for digit in str(digits)]

print(digits)

for digit in lista:
    if digit != 4 and digit != 7:
        lucky = False

if lucky:
    print("YES")
else:
    print("NO")

'''
Erro: 
input: 4744000695826
output: NO
answer: YES

Para que o número seja "nearly lucky", Petya não quer que a quantidade total de dígitos seja um "lucky number",
mas sim que o número de dígitos "lucky" seja um "lucky number".
'''
