size = int(input())

rows = size
column = size
matrix = []

for i in range(rows):
    matrix.append([])
    for j in [int(x) for x in input().split(' ')]:
        matrix[i].append(j)

print(sum([matrix[rows - row - 1][rows - row - 1] for row in range(rows)]))