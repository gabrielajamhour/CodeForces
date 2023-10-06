s1 = str(input())
s2 = str(input())

s1_minuscula = s1.lower()
s1_lista = s1_minuscula.split()
s2_minuscula = s2.lower()
s2_lista = s2_minuscula.split()

alfabeto_numeros = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

for i in range(len(s1_lista)):
    if s1_lista[i] > s2_lista[i]:
        print(1)
    elif s1_lista[i] < s2_lista[i]:
        print(-1)
    else:
        print(0)
