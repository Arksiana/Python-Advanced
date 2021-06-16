string = input()
n = int(input())
matrix = [[el for el in input()] for _ in range(n)]
player_index = 0
is_out = False


def is_eat(r, c, board):
    if board[r][c].isalpha():
        return True


# find player
for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'P':
            player_index = [row, col]
            matrix[row][col] = '-'

m = int(input())


def is_valid(r, c, size):
    if size > r >= 0 and size > c >= 0:
        return True


row = player_index[0]
col = player_index[1]
for _ in range(m):
    command = input()
    if command == 'left' and is_valid(row, col - 1, n):
        col = col - 1
        if is_eat(row, col, matrix):
            string += matrix[row][col]
            matrix[row][col] = '-'
    elif command == 'right' and is_valid(row, col + 1, n):
        col = col + 1
        if is_eat(row, col, matrix):
            string += matrix[row][col]
            matrix[row][col] = '-'
    elif command == 'up' and is_valid(row - 1, col, n):
        row = row - 1
        if is_eat(row, col, matrix):
            string += matrix[row][col]
            matrix[row][col] = '-'
    elif command == 'down':
        if is_valid(row + 1, col, n):
            row = row + 1
            if is_eat(row, col, matrix):
                string += matrix[row][col]
                matrix[row][col] = '-'
    else:
        string = string[:-1]
        is_out = True

    matrix[row][col] = 'P'
# if is_out:
#     string = string[:-1]
print(string)
for row in matrix:
    print(''.join(map(str, row)))
