t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    x = input()
    s = input()

    found = False

    for count in range(12):
        if s in x:
            found = True
            break
        else:
            x += x

    if found:
        print(count)
    else:
        print(-1)
