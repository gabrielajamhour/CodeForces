days = int(input())
money = list(map(int, input().split()))

seq = 1
current_seq = 1

for i in range(1, len(money)):
    if money[i] >= money[i - 1]:
        current_seq += 1
    else:
        current_seq = 1
    seq = max(seq, current_seq)

print(seq)
