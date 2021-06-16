# from itertools import chain
# from functools import lru_cache
#
# def read_matrix():
#     rows, cols = [int(el) for el in input().split()]
#     matrix = [[int(el) for el in input().split()] for _ in range(rows)]
#     return matrix
#
#
# def get_squares(matrix, size):
#     squares = []
#     for i in range(len(matrix) - (size - 1)):
#         row = matrix[i]
#         for j in range(len(row) - (size - 1)):
#             square = [
#                 matrix[i + n][j:j + size]
#                 for n in range(size)
#             ]
#             squares.append(square)
#     return squares
#
#
# def get_sum_of_matrix(matrix):
#     return f'Sum = {sum(chain(*matrix))}'
#
#
# def get_max_square(squares):
#     max_square_sum = None
#     max_square = None
#     for square in squares:
#         square_sum = get_sum_of_matrix(square)
#         if max_square_sum is None or square_sum > max_square_sum:
#             max_square_sum = square_sum
#             max_square = square
#     return max_square
#
#
# matrix = read_matrix()
# squares = get_squares(matrix, 3)
# max_square = get_max_square(squares)
#
#
# print(get_sum_of_matrix(max_square))
# print('\n'.join([' '.join(map(str, row)) for row in max_square]))
#
#

# FROM EXERCISE
rows, cols = [int(el) for el in input().split()]
matrix = [[int(el) for el in input().split()] for _ in range(rows)]
best_sum = - 99999
best_matrix = []
for row in range(rows - 2):
    for col in range(cols - 2):
        sub_matrix = []
        current_sum = 0
        row_counter = 0
        for r in range(row, row + 3):
            sub_matrix.append([])
            for c in range(col, col + 3):
                sub_matrix[row_counter].append(matrix[r][c])
                current_sum += matrix[r][c]
            row_counter += 1
        if current_sum > best_sum:
            best_sum = current_sum
            best_matrix = sub_matrix

print(f'Sum = {best_sum}')
for row in best_matrix:
    print(' '.join([str(el) for el in row]))

