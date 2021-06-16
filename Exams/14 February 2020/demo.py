def read_matrix():
    matrix = [[i for i in input().split(" ")] for el in range(n)]
    return matrix


def searching_for_the_player(row, col):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == "P":
                row = r
                col = c
                break

    return row, col


n = int(input())

# variables
coins = 0
path = []

# read matrix
matrix = read_matrix()

#
row = 0
col = 0
while not coins >= 100:
    command = input()
    # player position
    row, col = searching_for_the_player(row, col)
    searching_for_the_player(row, col)

    current_position = matrix[row][col]
    if 0 <= row < n - 1 and 0 <= col < n - 1:
        if command == "up":
            if 0 > row and n - 1 < col:
                if matrix[row - 1][col] == "X":
                    print(f"Game over! You've collected {round(coins / 2)} coins.")
                    break
                else:
                    coins += int(matrix[row - 1][col])
                    matrix[row][col] = "."
                    matrix[row - 1][col] = "P"
                    path.append(list(searching_for_the_player(row, col)))

            else:
                print(f"Game over! You've collected {round(coins / 2)} coins.")
                break
            break

        elif command == "down":
            if n - 1 > row and col in range(n - 1):

                if matrix[row + 1][col] == "X":
                    print(f"Game over! You've collected {round(coins / 2)} coins.")
                    break
                else:
                    coins += int(matrix[row + 1][col])
                    matrix[row][col] = "."
                    matrix[row + 1][col] = "P"
                    path.append(list(searching_for_the_player(row, col)))
            else:
                print(f"Game over! You've collected {round(coins / 2)} coins.")

        elif command == "right":
            if n - 1 > col and row in range(n - 1):
                if matrix[row][col + 1] == "X":
                    print(f"Game over! You've collected {round(coins / 2)} coins.")
                    break
                else:
                    coins += int(matrix[row][col + 1])
                    matrix[row][col] = "."
                    matrix[row][col + 1] = "P"
                    path.append(list(searching_for_the_player(row, col)))


            else:
                print(f"Game over! You've collected {round(coins / 2)} coins.")
                break
            break

        elif command == "left":
            if 0 < row and col in range(n - 1):
                if matrix[row][col - 1] == "X":
                    print(f"Game over! You've collected {round(coins / 2)} coins.")
                    break
                else:
                    coins += int(matrix[row][col - 1])
                    matrix[row][col] = "."
                    matrix[row][col - 1] = "P"
                    path.append(list(searching_for_the_player(row, col)))

            else:
                print(f"Game over! You've collected {round(coins / 2)} coins.")
                break
            break

        if coins >= 100:
            print(f"You won! You've collected {coins} coins.")
            break
        break
    else:
        print(f"Game over! You've collected {round(coins / 2)} coins.")
        break
    break

print("Your path:")
for el in path:
    print(el)
