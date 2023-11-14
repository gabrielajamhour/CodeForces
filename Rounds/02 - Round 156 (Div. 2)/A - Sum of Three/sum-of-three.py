t = int(input())

for _ in range(t):
    n = int(input())

    if n < 7:
        print("NO")
    elif n == 7:
        print("YES")
        print("1 2 4")
    elif n == 8:
        print("YES")
        print("1 2 5")
    elif n == 9:
        print("NO")
    
    elif n >= 10:
        if n % 3 == 0:
            print("YES")
            print(f"1 4 {n-5}")
        else:
            print("YES")
            print(f"1 2 {n-3}")
    



# Ele quer representar o número como uma soma de três inteiros positivos distintos
# Ele não quer que nenhum desses números sejam divididos por 3

# Tarefa:
    # Encontrar esses três números ou
    # Esses três números não existem

# n / 3 = False

# Não pode
# 3 6 9 12 15 18 21 24 27 30

# Pode
# 1 2 4 5 7 8 10 11 13 14

# 7
# 1 2 4

# 8
# 1 2 5

# Para o número 10
# para todos os numeros >= 10
    # no divisible = 1 2 n-3
    # divisible = 1 4 n-5

