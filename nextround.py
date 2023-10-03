""" Enunciado 
Você está organizando um concurso em que os n participantes avançam para a próxima rodada com base em suas pontuações.
Para avançar, um competidor deve ter uma pontuação igual ou superior à do k-ésimo colocado, desde que sua pontuação seja positiva.
Você já conhece as pontuações dos participantes.
Agora, seu objetivo é calcular quantos participantes avançarão para a próxima rodada com base nas regras do concurso.

Input
> Dois inteiros: n e k (1 ≤ k ≤ n ≤ 50), separados por um espaço.
> Uma sequência de n inteiros separados por espaços, representando as pontuações dos participantes (0 ≤ ai ≤ 100), onde ai é a pontuação do participante que ficou em i-ésimo lugar.

Output:
> Número de participantes que avançam para a próxima rodada. """

n_k = str(input()) # O usuário deve digitar n e k, separados por um espaço
# Como uma string não pode ser comparada com um valor inteiro em uma lista, transformamos em int

n_k_dividido = n_k.split() # Separamos a string com a função .split() en substrings
n = int(n_k_dividido[0]) # Atribui-se separadamente os valores de n e k como int
k = int(n_k_dividido[1])

# Assim como o primeiro input, o input das pontuações também é uma string que deve ser dividida em variáveis int
pontuacao = str(input()) # O usuário deve digitar as pontuações dos participantes, separadas por um espaço
pontuacao_dividida = pontuacao.split() 
totalparticipantes = [int(valor) for valor in pontuacao_dividida] # Esse comando transforma as substrings em ints e às coloca em uma lista

totalparticipantes.sort(reverse=True) # Colocar pontuações em ordem decrescente

PontuacoesMaiores = 0
for pontuacao in totalparticipantes: # Esse loop for é responsável por avaliar pontuação por pontuação se ela é maior ou igual à pontuação na k-ésima posição
    if pontuacao >= totalparticipantes[(k-1)] and totalparticipantes[(k-1)] != 0: # As posições em uma lista começam em 0, então é necessário subtrair 1 de k
        PontuacoesMaiores += 1
    elif totalparticipantes[(k-1)] == 0: 
        if pontuacao >= 1: # Se a pontuação do k-enésimo participante for 0, passam para próxima etapa os participantes com pontuação >= 1
            PontuacoesMaiores += 1

print(PontuacoesMaiores)
