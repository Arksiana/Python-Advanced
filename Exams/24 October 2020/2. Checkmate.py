board = [list(map(str, input().split())) for _ in range(8)]
""""
    "." – empty square
    "Q" – a queen
    "K" – the king
"""
king_index = 0
queen_index = 0
queen_indices = {}
move = ''

# find king indices
for row in range(len(board)):
    for col in range(len(board)):
        if board[row][col] == 'K':
            king_index = [row, col]


def canQueenAttack(qR, qC, oR, oC, move):
    move = ''
    # If queen and the opponent are
    # in the same row
    if qR == oR:
        move = 'same row'
        return move

        # If queen and the opponent are
    # in the same column
    if qC == oC:
        move = 'same column'
        return move

        # If queen can attack diagonally
    if abs(qR - oR) == abs(qC - oC):
        move = 'diagonally'
        return move

    # Opponent is safe
    return False


# find queen indices
for row in range(len(board)):
    for col in range(len(board)):
        if board[row][col] == 'Q':
            queen_index = (row, col)
            b = canQueenAttack(row, col, king_index[0], king_index[1], move)
            if b:
                queen_indices[queen_index] = b


flipped = {}

for key, value in queen_indices.items():
    if value not in flipped:
        flipped[value] = [key]
    else:
        flipped[value].append(key)

result = []
for k, v in flipped.items():
    if len(v) > 1:
        flipped[k].pop(1)

    result.append(list(v[0]))

if result:
    for el in result:
        print(el)
else:
    print("The king is safe!")



# Check Queen is blocked by another queen
# if queen_indices:
#     # current_row = queen_indices[0][0]
#     # current_col = queen_indices[0][1]
#
#
#     for k, v in queen_indices.items():
#         current_value = v
#
#     a = 5
#     for el in queen_indices:
#         if [current_row, current_col] != el:
#             if canQueenAttack(current_row, current_col, el[0], el[1], move):
#                 queen_indices.remove(el)
#             else:
#                 current_row = el[0]
#                 current_col = el[1]
#
#     for el in queen_indices:
#         print(el)
# else:
#     print("The king is safe!")
