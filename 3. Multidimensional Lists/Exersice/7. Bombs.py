n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
bomb_numbers = input().split()


def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def explode(row, col, size, m):
    b = m[row][col]
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if is_valid(r, c, size) and m[r][c] > 0:
                matrix[r][c] -= b


for bomb in bomb_numbers:
    tokens = [int(x) for x in bomb.split(',')]
    bomb_row = tokens[0]
    bomb_col = tokens[1]

    if matrix[bomb_row][bomb_col] > 0:
        explode(bomb_row, bomb_col, n, matrix)
        matrix[bomb_row][bomb_col] = 0

alive_cells = 0
alive_cells_sum = 0

for row in range(n):
    for col in range(n):
        number = matrix[row][col]
        if number > 0:
            alive_cells += 1
            alive_cells_sum += number

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_cells_sum}")
for row in matrix:
    print(' '.join(list(map(str, row))))
