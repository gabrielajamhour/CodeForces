initial_sum = str(input())
spaced_sum = initial_sum.replace('+',' ')
list_sum = spaced_sum.split()

list_sum = [int(num) for num in list_sum]

list_sum.sort()

list_sum = [str(num) for num in list_sum]
final_sum = '+'.join(list_sum)
print(final_sum)
