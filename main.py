board = ['-', ' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']
player1 = []
player2 = []
win = False


def write_board(board):
    print(f" {board[0]} | {board[0]} | {board[0]}")
    print(f" {board[1]} | {board[2]} | {board[3]}")
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print(f" {board[7]} | {board[8]} | {board[9]}")
    print(f" {board[0]} | {board[0]} | {board[0]}")


def choose_mark():
    while True:
        answer = input("Player 1: Choose your marker 'X' or 'O' - ")
        if answer.upper() == 'X':
            player1.append('X')
            player2.append('O')
            print(player1, player2)
            break
        elif answer.upper() == 'O':
            player1.append('O')
            player2.append('X')
            print(player1, player2)
            break
        else:
            print("Wrong answer")


def choose_position(win):
    while not win:
        while True:
            p1 = int(input("Choose position(1-9)(player 1):"))
            if board[p1] == ' ' or board[p1] != player2[0]:
                board[p1] = player1[0]
                write_board(board)
                break
            else:
                print("This position is incorrect")
                continue
        win = check_win(player1[0])
        full_board = check_full_board(board)
        if win:
            print("Player 1 win")
            break
        elif full_board:
            print("Draw")
            break
        while True:
            p2 = int(input("Choose position(1-9)(player 2):"))
            if board[p2] == ' ' or board[p1] != player1[0]:
                board[p2] = player2[0]
                write_board(board)
                break
            else:
                print("This position is incorrect")
                continue
        win = check_win(player2[0])
        if win:
            print("Player 2 win")
            break
    print('End game')


def check_win(mark):
    # row
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    # column
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    # cross
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False


def check_full_board(board):
    if ' ' not in board:
        return True

if __name__ == '__main__':
    choose_mark()
    choose_position(win)
    check_full_board(board)