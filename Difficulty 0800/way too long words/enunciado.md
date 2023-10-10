Às vezes, algumas palavras como “ localização ” ou “ internacionalização ” são tão longas que escrevê-las muitas vezes em um texto é bastante cansativo.  
Vamos considerar uma palavra muito longa se seu comprimento for estritamente superior a 10 caracteres. Todas as palavras muito longas devem ser substituídas por uma abreviatura especial.  
Essa abreviatura é feita assim: escrevemos a primeira e a última letra de uma palavra e entre elas escrevemos a quantidade de letras entre a primeira e a última letra. Esse número está no sistema decimal e não contém zeros à esquerda.  
Assim, “ localização ” será escrita como “ l10n ”, e “ internacionalização ” será escrita como “ i18n ”.  
Sugere-se que você automatize o processo de alteração das palavras com abreviações. Nesse sentido, palavras muito longas deverão ser substituídas pela abreviatura e as palavras não muito longas não deverão sofrer alterações.

Input  
A primeira linha contém um inteiro n ( 1 ≤  n  ≤ 100 ). Cada uma das n linhas a seguir contém uma palavra. Todas as palavras consistem em letras latinas minúsculas e possuem comprimentos de 1 a 100 caracteres.

Output  
Imprima n linhas. A i -ésima linha deve conter o resultado da substituição da i -ésima palavra dos dados de entrada.
