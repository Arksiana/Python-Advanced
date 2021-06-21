def is_valid(m, r, c):
    if 0 <= r < len(m) and 0 <= c < len(m):
        return True
    return False


def play(b, r, c):
    if b[r][c] == 'D':
        return 2 * (int(b[0][c]) + int(b[6][c]) + int(b[r][0]) + int(b[r][6]))
    elif b[r][c] == 'T':
        return 3 * (int(b[0][c]) + int(b[6][c]) + int(b[r][0]) + int(b[r][6]))

    elif b[r][c].isalnum():
        return int(b[r][c])


first_name, second_name = input().split(', ')
board = [input().split() for _ in range(7)]
first_points = 501
second_points = 501
turns = 0

win = False

while True:
    turns += 1
    first_shot = input().split()
    row, col = int(first_shot[0][1]), int(first_shot[1][0])
    if is_valid(board, row, col):
        if board[row][col] == 'B':
            print(f"{first_name} won the game with {turns} throws!")
            break
        first_points -= play(board, row, col)
        if first_points <= 0:
            print(f"{first_name} won the game with {turns} throws!")
            break

    second_shot = input().split()
    row, col = int(second_shot[0][1]), int(second_shot[1][0])
    if is_valid(board, row, col):
        if board[row][col] == 'B':
            print(f"{second_name} won the game with {turns} throws!")
            break
        second_points -= play(board, row, col)
        if second_points <= 0:
            print(f"{second_name} won the game with {turns} throws!")
            break
