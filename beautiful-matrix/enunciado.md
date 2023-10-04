Você tem uma matriz 5 × 5 , composta por 24 zeros e um único número um. Vamos indexar as linhas da matriz por números de 1 a 5 de cima para baixo, vamos indexar as colunas da matriz por números de 1 a 5 da esquerda para a direita. Em um movimento, você pode aplicar uma das duas transformações a seguir à matriz:

1. Troque duas linhas da matriz vizinhas, ou seja, linhas com índices i e i  + 1 por algum inteiro i (1 ≤  i  < 5)
2. Troque duas colunas de matrizes vizinhas, ou seja, colunas com índices j e j  + 1 por algum inteiro j (1 ≤  j  < 5)

Você acha que uma matriz fica bonita se o único número um da matriz estiver localizado no meio (na célula que está na interseção da terceira linha e da terceira coluna). Conte o número mínimo de movimentos necessários para deixar a matriz bonita.

Input  
A entrada consiste em cinco linhas, cada linha contém cinco inteiros: o j -ésimo inteiro na i -ésima linha da entrada representa o elemento da matriz que está localizado na interseção da i -ésima linha e da j -ésima coluna. É garantido que a matriz consiste em 24 zeros e um único número um.

Output  
Imprima um único número inteiro – o número mínimo de movimentos necessários para deixar a matriz bonita.
