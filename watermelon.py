""" Enunciado
  Em um dia quente de verão, Pete e Billy querem dividir uma melancia de peso w.
  Eles desejam que cada parte tenha um peso par, mas não necessariamente igual. 
  Ajude-os a determinar se isso é possível.

> Input:
    Um único número inteiro w (1 ≤ w ≤ 100) representando o peso da melancia.
> Output:
    Imprima "YES" se for possível dividir a melancia em duas partes, cada uma com um peso par.
    Imprima "NO" caso contrário. """

w = int(input())

# Para que ambas as partes tenham um peso par, é necessário que w seja par e maior que 2.
if w%2==0 and w<=100 and w>2:
    print("YES")
else:
    print("NO")
