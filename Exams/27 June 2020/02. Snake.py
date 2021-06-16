n = int(input())
field = [list(input()) for _ in range(n)]
snake_index = 0
eaten_food = 0


def if_eat_food(board, s_index):
    row = s_index[0]
    col = s_index[1]
    if board[row][col] == '*':
        return True
    return False


def is_out_field(s_index, size):
    row = s_index[0]
    col = s_index[1]
    if 0 <= row < size and 0 <= col < size:
        return False
    return True


def move_snake(board, move, s_index, food):
    row = s_index[0]
    col = s_index[1]
    moves_list = {'up': [row - 1, col], 'down': [row + 1, col], 'left': [row, col - 1], 'right': [row, col + 1]}
    if move in moves_list:
        current = moves_list[move]
        s_index = current

        return s_index
    return s_index


# command_list = ['up', 'down', 'left', 'right']
# move_list = {'up': [col  - 1], 'down': [col + 1], 'left': [row - 1], 'right': [row + 1]}

# find snake - S
for row in range(n):
    for col in range(n):
        if field[row][col] == 'S':
            snake_index = [row, col]

while True:
    command = input()
    snake_index = move_snake(field, command, snake_index, eaten_food)
    print(snake_index)

    if if_eat_food(field, snake_index):
        eaten_food += 1
        if eaten_food == 10:
            break

    if is_out_field(snake_index, n):
        break
