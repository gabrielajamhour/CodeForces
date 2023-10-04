w = int(input())

# Para que ambas as partes tenham um peso par, é necessário que w seja par e maior que 2.
if w%2==0 and w<=100 and w>2:
    print("YES")
else:
    print("NO")
