matrix = [list(map(int, input().split())) for _ in range(int(input()))]

data = input()
while not data == 'END':
    command, row, col, value = data.split()
    row, col, value = int(row), int(col), int(value)

    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        if command == 'Add':
            matrix[row][col] += value
        elif command == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')

    data = input()

[print(*row) for row in matrix]
