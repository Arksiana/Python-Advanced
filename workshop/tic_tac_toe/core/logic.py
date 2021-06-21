from workshop.tic_tac_toe.core.validators import *
from workshop.tic_tac_toe.core.helpers import get_row_col


def play(players, board, turns):
    current_turn_count = 1
    while True:
        current_player_name = turns[current_turn_count % 2]
        # read position
        position = int(input(f"{current_player_name} choose a free position"))

        # check if is in range
        if is_position_in_range(position):
            if is_place_available(board, position):
                row, col = get_row_col(position)
                board[row][col] = players[current_player_name]
            pass
            # check is there is a winner
        else:
            # read new position for the same players
            pass

        # check if place is available
        # check is there is a winner
        pass
