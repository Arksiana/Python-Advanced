from workshop.tic_tac_toe.core.costants import position_mapper
from workshop.tic_tac_toe.core.helpers import get_row_col

def is_position_in_range(position):
    if 1 <= position <= 9:
        return True
    return False


def is_place_available(board, position):
    row, col = get_row_col(position)
    if not board[row][col] == ' ':
        return False
    return True
