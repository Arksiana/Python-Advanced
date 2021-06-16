rows, columns = [int(x) for x in input().split(', ')]

matrix = []
max_sum_square = 0
square_matrix = []

for i in range(rows):
    matrix.append([])
    for j in [int(x) for x in input().split(', ')]:
        matrix[i].append(j)

for i in range(rows - 1):
    for j in range(columns - 1):
        current_sum = matrix[i][j] + matrix[i + 1][j] + matrix[i][j + 1] + matrix[i + 1][j + 1]
        if current_sum > max_sum_square:
            max_sum_square = current_sum
            square_matrix = [[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]]

for el in square_matrix:
    for ele in el:
        print(ele, end=' ')
    print()
print(max_sum_square)