word = str(input())

# Definir 'hello' como o objetivo para se encontrar
target = 'hello'

i = 0 # Índice da palavra de entrada
j = 0 # Índice da sequência 'hello'

while i < len(word) and j < len(target):
    if word[i] == target[j]:
        j += 1  
    i += 1

if j == len(target):
    print("YES")
else:
    print("NO")   
