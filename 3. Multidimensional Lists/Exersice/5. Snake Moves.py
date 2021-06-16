from collections import deque

rows, cols = [int(el) for el in input().split()]
text = deque(input())
matrix = [['' for el in range(cols)] for _ in range(rows)]

for row in range(rows):
    for col in range(cols):
        current_col = col
        current_char = text.popleft()
        if row % 2 != 0:
            current_col = cols - 1 - col
        matrix[row][current_col] = current_char
        text.append(current_char)

for row in matrix:
    print(''.join(row))