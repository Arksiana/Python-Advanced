DEFAULT_ROWS_COUNT = 6
DEFAULT_COLUMNS_COUNT = 7
DEFAULT_WIN_CONDITION = 4


def get_player_choice_func(is_test=False):
    def get_player_choice(player):
        print(f"Player {player}, please choose a column")
        return int(input()) - 1

    #
    # choices_for_test = [1, 2, 2, 3, 3, 4, 1, 5]  # horizontal win
    # choices_for_test = [1, 2, 1, 2, 1, 2, 1, 2]  # vertical win
    choices_for_test = [1, 2, 1, 4, 3, 3, 3, 7, 4, 4, 4]  # diagonal win
    choices_for_test_index = 0

    def get_player_choice_for_test(player):
        nonlocal choices_for_test_index
        print(f"Player {player}, please choose a column")
        choice = choices_for_test[choices_for_test_index]
        print(choice)
        choices_for_test_index += 1
        return choice - 1

    if is_test:
        return get_player_choice_for_test
    else:
        return get_player_choice


def get_lowest_free_row_func():
    free_row_indices = []

    def get_lowest_free_row_index(board, column_index):
        while len(free_row_indices) < column_index:
            free_row_indices.append(0)
        row_index = len(board) - free_row_indices[column_index] - 1
        free_row_indices[column_index] += 1
        return row_index
    return get_lowest_free_row_index


def apply_player_choice(board, column_index, player):
    row_index = get_lowest_free_row_index(board, column_index)
    board[row_index][column_index] = player
    return row_index, column_index


def in_range(value, max_value):
    return 0 <= value < max_value


def is_win_condition_value(board, row_index, column_index, player, rows_count, columns_count):
    return in_range(row_index, rows_count) and in_range(column_index, columns_count) and board[row_index][
        column_index] == player


def has_win_condition(board, player, row_index, column_index, win_condition_count=DEFAULT_WIN_CONDITION):
    columns_count = len(board)
    rows_count = len(board[0])

    left_horizontal_values = [
        is_win_condition_value(board, row_index, column_index + d, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    right_horizontal_values = [
        is_win_condition_value(board, row_index, column_index - d, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    down_vertical_values = [
        is_win_condition_value(board, row_index + d, column_index, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    up_vertical_values = [is_win_condition_value(board, row_index - d, column_index, player, rows_count, columns_count)
                          for d in range(win_condition_count)]

    down_left_diagonal_values = [
        is_win_condition_value(board, row_index + d, column_index - d, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    down_right_diagonal_values = [
        is_win_condition_value(board, row_index + d, column_index + d, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    up_left_diagonal_values = [
        is_win_condition_value(board, row_index - d, column_index - d, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    up_right_diagonal_values = [
        is_win_condition_value(board, row_index - d, column_index + d, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    results = [
        all(left_horizontal_values),
        all(right_horizontal_values),
        all(down_vertical_values),
        all(up_vertical_values),
        all(down_left_diagonal_values),
        all(down_right_diagonal_values),
        all(up_left_diagonal_values),
        all(up_right_diagonal_values)
    ]

    return any(results)


def print_board(board):
    for row in board:
        print(row)


def print_winner_message(player):
    print(f"The winner is player {player}")


def play(board, player=1):
    while True:
        player_choice = get_player_choice(player)
        (row_index, column_index) = apply_player_choice(board, player_choice, player)
        print_board(board)
        if has_win_condition(board, player, row_index, column_index):
            print_winner_message(player)
            break
        player = 2 if player == 1 else 1

    # else:
    #     play(board, player=2)


def create_board(rows_count=DEFAULT_ROWS_COUNT, columns_count=DEFAULT_COLUMNS_COUNT):
    return [[0] * columns_count for _ in range(rows_count)]


get_player_choice = get_player_choice_func(is_test=True)
board = create_board()

play(board)
