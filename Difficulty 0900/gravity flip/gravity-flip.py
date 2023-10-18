cubes = int(input())
num_cubes = list(map(int, input().split()))

num_cubes.sort()
num_cubes = [str(num) for num in num_cubes]

print(' '.join(num_cubes))
