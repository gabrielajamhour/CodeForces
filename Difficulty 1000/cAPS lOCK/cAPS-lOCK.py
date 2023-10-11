palavra = str(input())

if palavra.upper() == palavra:
    print(palavra.lower())
elif palavra[0].lower() + palavra[1:].upper() == palavra:
    lower_word = palavra.lower()
    capitalize_word = palavra.capitalize()
    print(capitalize_word)
else:
    print(palavra)
