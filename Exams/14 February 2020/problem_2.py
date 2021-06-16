import math

n = int(input())
matrix = [input().split() for _ in range(n)]

path = []
coins = 0
won = False
player_index = [[row, col] for row in range(n) for col in range(n) if matrix[row][col] == 'P'][0]


def valid_move(r, c, m):
    if len(m) > r >= 0 and len(m) > c >= 0:
        return True
    return False


def move_player(r, c, m):
    if valid_move(r, c, m):
        if m[r][c] == 'X':
            return False
    if not valid_move(r, c, m):
        return False
    return True


while True:
    if coins >= 100:
        won = True
        break

    command = input()
    move = [player_index[0], player_index[1]]
    if command == 'up':
        if move_player(player_index[0] - 1, player_index[1], matrix):
            coins += int(matrix[player_index[0] - 1][player_index[1]])
            player_index = [player_index[0] - 1, player_index[1]]
            path.append(player_index)
        else:
            coins = math.floor(coins / 2)
            break

    elif command == 'down':
        if move_player(player_index[0] + 1, player_index[1], matrix):
            coins += int(matrix[player_index[0] + 1][player_index[1]])
            player_index = [player_index[0] + 1, player_index[1]]
            path.append(player_index)

        else:
            coins = math.floor(coins / 2)
            break

    elif command == 'right':
        if move_player(player_index[0], player_index[1] + 1, matrix):
            coins += int(matrix[player_index[0]][player_index[1] + 1])
            player_index = [player_index[0], player_index[1] + 1]
            path.append(player_index)

        else:
            coins = math.floor(coins / 2)
            break

    elif command == 'left':
        if move_player(player_index[0], player_index[1] - 1, matrix):
            coins += int(matrix[player_index[0]][player_index[1] - 1])
            player_index = [player_index[0], player_index[1] - 1]
            path.append(player_index)

        else:
            coins = math.floor(coins / 2)
            break

if won:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print('Your path:')
print(*path, sep='\n')


