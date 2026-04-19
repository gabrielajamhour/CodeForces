# Para printar todos os outputs só no final
test_cases = int(input())
results = []

for _ in range(test_cases):

    hay = "NO"
    for color in coloresbombones:
        if colorfavorito == color:
            hay = "YES"
    results.append(hay)

for result in results:
    print(result)
