from pprint import pprint

rows, cols = [int(el) for el in input().split()]
matrix = [list(map(int, input().split())) for _ in range(rows)]

pprint(matrix)
