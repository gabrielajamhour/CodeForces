cost_1stbanana, num_dollars, num_bananas = map(int, input().split())

totalcost = 0
for i in range(num_bananas + 1):
    totalcost += cost_1stbanana * i

if num_dollars > totalcost:
    print(0)
else:
    print(totalcost - num_dollars)
