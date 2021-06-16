rows, cols = [int(el) for el in input().split(', ')]
matrix = [[int(el) for el in input().split()] for _ in range(rows)]

for j in range(cols):
    total = sum(row[j] for row in matrix)
    print(total)
