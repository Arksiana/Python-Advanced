rows, cols = [int(el) for el in input().split(", ")]
matrix = [
    [int(el) for el in input().split()]
    for _ in range(rows)
]

for col in zip(*matrix):
    print(col)