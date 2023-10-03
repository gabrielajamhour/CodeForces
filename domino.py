""" Enunciado 
Você recebe um tabuleiro retangular de M x N quadrados e um número ilimitado de peças de dominó padrão, cada uma com dois quadrados.
A tarefa é posicionar essas peças no tabuleiro de forma a cobrir o máximo possível de quadrados, seguindo as regras fornecidas:
  1. Não há dominós sobrepostos
  2. Cada peça deve estar inteiramente dentro do tabuleiro
O desafio é encontrar o número máximo de dominós que podem ser colocados.

Input: 
> Dois inteiros: M e N (1 ≤ M ≤ N ≤ 16), representando as dimensões de um tabuleiro retangular.
Output:
> Número máximo de dominós 2 × 1 que podem ser colocados no tabuleiro, seguindo as condições especificadas. """

M_N = str(input()) # O usuário deve digitar M e N, separados por um espaço
# Para tratar M e N como variáveis independentes e, tendo em vista que se tratam de números inteiros, transformamos em int

M_N_dividido= M_N.split() # Separamos a string com a função .split() en substrings
M = int(M_N_dividido[0]) # Atribui-se separadamente os valores de M e N como int
N = int(M_N_dividido[1])

area = M * N 
dominos = area // 2

print(dominos)
