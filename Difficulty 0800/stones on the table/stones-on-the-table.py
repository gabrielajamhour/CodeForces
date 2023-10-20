num_stones = int(input())
color_stones = str(input())
color_stones = [color for color in color_stones]

same = 0

for i in range(len(color_stones) - 1):
    if color_stones[i] == color_stones[i + 1]:
        same += 1

print(same)
