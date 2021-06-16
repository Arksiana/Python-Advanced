def multiply_bunny(row, column, matrix):
    try:
        if not matrix[row][column + 1] == 'B' and row >= 0 and column + 1 >= 0:
            matrix[row][column + 1] = 'B'
    except:
        IndexError
    try:
        if not matrix[row][column - 1] == 'B' and row >= 0 and column - 1 >= 0:
            matrix[row][column - 1] = 'B'
    except:
        IndexError
    try:
        if not matrix[row - 1][column] == 'B' and row - 1 >= 0 and column >= 0:
            matrix[row - 1][column] = 'B'
    except:
        IndexError
    try:
        if not matrix[row + 1][column] == 'B' and row + 1 >= 0 and column >= 0:
            matrix[row + 1][column] = 'B'
    except:
        IndexError
    return matrix


n, m = map(int, input().split())

rows = n
columns = m
matrix = []
player = 'alive'
b_indexes = []

for i in range(rows):
    matrix.append([])
    matrix[i] += list(input())

commands = input()

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == 'P':
            matrix[i][j] = '.'
            row = i
            column = j

for el in commands:

    b_indexes = []

    for k in range(rows):
        for l in range(columns):
            if matrix[k][l] == 'B':
                b_indexes.append((k, l))

    for ele in b_indexes:
        multiply_bunny(ele[0], ele[1], matrix)

    if el == 'U':
        if 0 <= row - 1 < rows and 0 <= column < columns:
            if matrix[row - 1][column] == 'B':
                player = 'dead'
                row -= 1
                break
            else:
                row -= 1
        else:
            player = 'won'
            break
    elif el == 'R':
        if 0 <= row < rows and 0 <= column + 1 < columns:
            if matrix[row][column + 1] == 'B':
                player = 'dead'
                column += 1
                break
            else:
                column += 1
        else:
            player = 'won'
            break
    elif el == 'D':
        if 0 <= row + 1 < rows and 0 <= column < columns:
            if matrix[row + 1][column] == 'B':
                player = 'dead'
                row += 1
                break
            else:
                row += 1
        else:
            player = 'won'
            break
    elif el == 'L':
        if 0 <= row < rows and 0 <= column - 1 < columns:
            if matrix[row][column - 1] == 'B':
                player = 'dead'
                column -= 1
                break
            else:
                column -= 1
        else:
            player = 'won'
            break

[print(*row, sep='') for row in matrix]
if player == 'won':
    print(f'won: {row} {column}')
elif player == 'dead':
    print(f'dead: {row} {column}')