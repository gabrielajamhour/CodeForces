initial_sum = str(input())
spaced_sum = initial_sum.replace('+',' ')
list_sum = spaced_sum.split()

list_sum = [int(num) for num in list_sum]

list_sum.sort() # Para aplicar a função .sort(), é necessário que os elementos sejam int

list_sum = [str(num) for num in list_sum] # Para juntar os elementos por um '+', é necessário que sejam strings de volta
final_sum = '+'.join(list_sum)
print(final_sum)
