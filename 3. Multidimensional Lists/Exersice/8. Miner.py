n = int(input())
commands = input().split()
matrix = [[x for x in input().split()] for _ in range(n)]
coals = 0
total_coals = 0
minor_position = []
end = False

for row in range(len(matrix)):
    if 's' in matrix[row]:
        minor_position = [row, matrix[row].index('s')]
    total_coals += matrix[row].count('c')

for command in commands:
    next_minor_position = []
    if command == 'up':
        next_minor_position = [minor_position[0] - 1, minor_position[1]]
    elif command == 'down':
        next_minor_position = [minor_position[0] + 1, minor_position[1]]
    elif command == 'left':
        next_minor_position = [minor_position[0], minor_position[1] - 1]
    elif command == 'right':
        next_minor_position = [minor_position[0], minor_position[1] + 1]

    # check indexes
    if 0 <= next_minor_position[0] < len(matrix) and 0 <= next_minor_position[1] < len(matrix):
        row = next_minor_position[0]
        col = next_minor_position[1]
        if matrix[row][col] == '*':
            matrix[minor_position[0]][minor_position[1]] = '*'
            matrix[row][col] = 's'
            minor_position = next_minor_position
        elif matrix[row][col] == 'e':
            print(f'Game over! ({row}, {col})')
            end = True
            break
        elif matrix[row][col] == 'c':
            coals += 1
            if coals == total_coals:
                print(f'You collected all coals! ({row}, {col})')
                end = True
                break
            matrix[minor_position[0]][minor_position[1]] = '*'
            matrix[row][col] = 's'
            minor_position = next_minor_position


if not end:
    print(f"{total_coals - coals} coals left. ({minor_position[0]}, {minor_position[1]})")