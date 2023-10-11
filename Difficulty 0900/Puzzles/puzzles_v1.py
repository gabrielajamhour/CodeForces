students, puzzles = map(int, input().split())
# Sem a função map(), seria impressa uma lista de strings

pieces = list(map(int, input().split()))
pieces.sort()

print(pieces)

sub_pieces = pieces[:students]
# Faz com que sejam selecionadas os x primeiros puzzles, onde x = students

print(sub_pieces)

if students == 2 and len(pieces) != len(set(pieces)):
    print("0")
else:
    difference = sub_pieces[-1] - sub_pieces[0]    
    print(difference)
