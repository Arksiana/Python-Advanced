n = int(input())
n_bombs = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

direction = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
    'up_left': [-1, -1],
    'up_right': [-1, 1],
    'down_left': [1, -1],
    'down_right': [1, 1]

}


def check_index(matrix, r, c):
    if len(matrix) > r >= 0 and len(matrix) > c >= 0:
        return True
    return False


def place_bombs(matrix, r, c):
    if check_index(matrix, r, c):
        matrix[r][c] = '*'
        return matrix


def calculate_numbers(matrix, r, c):
    for k, v in direction.items():
        to_row = int(v[0]) + r
        to_col = int(v[1]) + c
        if check_index(matrix, to_row, to_col) and matrix[to_row][to_col] != '*':
            matrix[to_row][to_col] += 1
    return matrix


for _ in range(n_bombs):
    row, col = map(int, input().strip('()').split(", "))
    board = place_bombs(board, row, col)
    board = calculate_numbers(board, row, col)

[print(' '.join(list(map(str, x)))) for x in board]

# n_matrix = int(input())
# bombs = int(input())
#
#
# def check_index(r, c):
#     if n_matrix > r >= 0 and n_matrix > c >= 0 and matrix[r][c] != '*':
#         return True
#     return False
#
#
# matrix = [[0 for _ in range(n_matrix)] for _ in range(n_matrix)]
# for bomb in range(bombs):
#     row, col = map(int, input().strip('()').split(", "))
#
#     matrix[row][col] = '*'
#
#     if check_index(row - 1, col - 1):
#         matrix[row - 1][col - 1] += 1
#     if check_index(row - 1, col):
#         matrix[row - 1][col] += 1
#     if check_index(row - 1, col + 1):
#         matrix[row - 1][col + 1] += 1
#     if check_index(row, col + 1):
#         matrix[row][col + 1] += 1
#     if check_index(row, col - 1):
#         matrix[row][col - 1] += 1
#     if check_index(row + 1, col - 1):
#         matrix[row + 1 ][col - 1] += 1
#     if check_index(row + 1, col):
#         matrix[row + 1][col] += 1
#     if check_index(row + 1, col + 1):
#         matrix[row + 1][col + 1] += 1
#
# for row in matrix:
#     print(' '.join(map(str, row)))
