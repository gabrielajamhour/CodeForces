M_N = str(input()) # O usuário deve digitar M e N, separados por um espaço
# Para tratar M e N como variáveis independentes e, tendo em vista que se tratam de números inteiros, transformamos em int

M_N_dividido= M_N.split() # Separamos a string com a função .split() en substrings
M = int(M_N_dividido[0]) # Atribui-se separadamente os valores de M e N como int
N = int(M_N_dividido[1])

area = M * N 
dominos = area // 2

print(dominos)
