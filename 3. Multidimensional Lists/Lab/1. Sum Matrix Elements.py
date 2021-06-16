import itertools
rows, cows = [int(el) for el in input().split(', ')]
matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]
total = sum(itertools.chain(*matrix))
print(total)
print(matrix)


