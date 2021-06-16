n_matrix = int(input())
bombs = int(input())


def check_index(r, c):
    if n_matrix > r >= 0 and n_matrix > c >= 0 and matrix[r][c] != '*':
        return True
    return False


matrix = [[0 for _ in range(n_matrix)] for _ in range(n_matrix)]
for bomb in range(bombs):
    row, col = map(int, input().strip('()').split(", "))

    matrix[row][col] = '*'

    if check_index(row - 1, col - 1):
        matrix[row - 1][col - 1] += 1
    if check_index(row - 1, col):
        matrix[row - 1][col] += 1
    if check_index(row - 1, col + 1):
        matrix[row - 1][col + 1] += 1
    if check_index(row, col + 1):
        matrix[row][col + 1] += 1
    if check_index(row, col - 1):
        matrix[row][col - 1] += 1
    if check_index(row + 1, col - 1):
        matrix[row + 1 ][col - 1] += 1
    if check_index(row + 1, col):
        matrix[row + 1][col] += 1
    if check_index(row + 1, col + 1):
        matrix[row + 1][col + 1] += 1

for row in matrix:
    print(' '.join(map(str, row)))
