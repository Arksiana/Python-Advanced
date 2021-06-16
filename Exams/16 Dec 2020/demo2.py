from IPython.display import clear_output
from random import randint


# def choose_first():
#     flip = randint(0,1)
#     if flip == 0:
#         print("PLAYER ONE GOES FIRST")

def rematch(choice):
    while not choice == "No" and choice == "Yes":
        if choice == "No":
            return False
        elif choice == "Yes":
            return player_1_choice(player_one, player_two)


def player_1_choice(p1, p2):
    while not p1 == "X" and not p1 == "O":
        mark = input("Please pick a marker X or O ?")
        if mark == "X":
            p1 = "X"
            p2 = "O"
        elif mark == "O":
            p2 = "X"
            p1 = "O"
    return (p1, p2)


def display_board(board):
    clear_output()
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("_____")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("_____")
    print(board[6] + "|" + board[7] + "|" + board[8])
    return board


def winner_check(board, mark):
    if (board[0] == mark and board[1] == mark and board[2] == mark) or \
            (board[3] == mark and board[4] == mark and board[5] == mark) or \
            (board[6] == mark and board[7] == mark and board[8] == mark) or \
            (board[0] == mark and board[3] == mark and board[6] == mark) or \
            (board[1] == mark and board[4] == mark and board[7] == mark) or \
            (board[2] == mark and board[5] == mark and board[8] == mark) or \
            (board[0] == mark and board[4] == mark and board[8] == mark) or \
            (board[2] == mark and board[4] == mark and board[6] == mark):
        return True
    return False


def board_insert(board, move, marker, history):
    # move_history = []
    while move in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        if move not in history:
            history.append(move)
            board[move] = marker
            # return board
        else:
            print("сори майка тука вече е играно")
            break
        return board


is_draw = False
player_one = ""
player_two = ""
player_one, player_two = player_1_choice(player_one, player_two)
draw_check = 0
board = ["-"] * 9
move_history = []

while True:

    player_one_turn = int(input("It's your turn player one"))
    draw_check += 1
    board_insert(board, player_one_turn, player_one, move_history)
    if draw_check == 9 and not winner_check(board, player_one):
        print("DRAW!")
        re = input("Play again? Yes or No?")
        board = ["-"] * 10
        rematch(re)
        if not rematch(re):
            break

    display_board(board)
    if winner_check(board, player_one):
        print("CONGRATULATIONS TO YOU,PLAYER ONE!")
        re = input("Play again? Yes or No?")
        board = ["-"] * 10
        if not rematch(re):
            break

    player_two_turn = int(input("It's your turn player two"))
    draw_check += 1
    board_insert(board, player_two_turn, player_two, move_history)
    display_board(board)
    if winner_check(board, player_two):
        print("CONGRATULATIONS TO YOU,PLAYER TWO!")
        re = input("Play again? Yes or no?")
        board = ["-"] * 10
        rematch(re)
        if not rematch(re):
            break
    if draw_check == 9 and not winner_check(board, player_two):
        print("DRAW!")
        re = input("Play again? Yes or no?")
        board = ["-"] * 10
        rematch(re)
        if not rematch(re):
            break