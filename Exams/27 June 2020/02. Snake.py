n = int(input())
field = [list(input()) for _ in range(n)]
snake_index = 0
eaten_food = 0


def if_eat_food(board, s_index):
    row = s_index[0]
    col = s_index[1]
    if board[row][col] == '*':
        board[row][col] = '.'
        return True
    return False


def is_out_field(s_index, size):
    row = s_index[0]
    col = s_index[1]
    if 0 <= row < size and 0 <= col < size:
        return False
    return True


def move_snake(move, s_index):
    row = s_index[0]
    col = s_index[1]
    moves_list = { 'up': [row - 1, col], 'down': [row + 1, col], 'left': [row, col - 1], 'right': [row, col + 1] }
    if move in moves_list:
        s_index = moves_list[move]
        return s_index
    return s_index


# find snake - S
for row in range(n):
    for col in range(n):
        if field[row][col] == 'S':
            snake_index = [row, col]
            field[row][col] = '.'


def in_trap(board, s_index):
    row = s_index[0]
    col = s_index[1]
    if board[row][col] == 'B':
        board[row][col] = '.'
        return True

    return False


while True:
    command = input()
    snake_index = move_snake(command, snake_index)

    if not is_out_field(snake_index, n):

        if if_eat_food(field, snake_index):
            eaten_food += 1
            if eaten_food == 10:
                field[snake_index[0]][snake_index[1]] = 'S'
                print("You won! You fed the snake.")
                break

        elif in_trap(field, snake_index):
            row = snake_index[0]
            col = snake_index[1]
            for r in range(n):
                for c in range(n):
                    if field[r][c] == 'B' and r != row and c != col:
                        snake_index = [r, c]
                        field[snake_index[0]][snake_index[1]] = '.'
        else:
            row = snake_index[0]
            col = snake_index[1]
            field[snake_index[0]][snake_index[1]] = '.'

    if is_out_field(snake_index, n):
        print("Game over!")
        break

print(f"Food eaten: {eaten_food}")
for el in field:
    print(*el, sep='')
