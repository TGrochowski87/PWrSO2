""" Random """
import random


def welcome_info():
    """ Game info """

    print("  WELCOME\n")
    print("Key bindings:")
    print(" Q | W | E")
    print(" A | S | D")
    print(" Z | X | C")
    print("\n")



def print_board(board):
    """ Displaying board """

    for i in range(3):
        for j in range(3):
            print(board[i][j] + " ", end='')
        print()
    print("\n")



def is_board_full(board):
    """ Checking if board has no available spaces """

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return False
    return True



def check_win_condition(board, character):
    """ Checking if any player won """

    for i in range(3):
        if board[i][0] == character and board[i][1] == character and board[i][2] == character:
            return True

    for i in range(3):
        if board[0][i] == character and board[1][i] == character and board[2][i] == character:
            return True

    if board[0][0] == character and board[1][1] == character and board[2][2] == character:
        return True

    if board[0][2] == character and board[1][1] == character and board[2][0] == character:
        return True

    return False



def player_turn(board, keys, player_char):
    """ Functionality for player's turn """

    if is_board_full(board):
        return

    while True:
        place = input("Choose position ")

        if not place in keys:
            print("Wrong position given!")
            continue

        board_x, board_y = keys[place]

        if board[board_x][board_y] != '_':
            print("Position already taken!")
        else:
            board[board_x][board_y] = player_char
            break



def computer_turn(board, computer_char, player_char):
    """ Functionality for computer's turn """

    if is_board_full(board):
        return

    ## WIN CONDITION
    # =
    for i in range(3):
        if board[i][0] == computer_char and board[i][1] == computer_char:
            if board[i][2] == '_':
                board[i][2] = computer_char
                return

        if board[i][1] == computer_char and board[i][2] == computer_char:
            if board[i][0] == '_':
                board[i][0] = computer_char
                return

        if board[i][0] == computer_char and board[i][2] == computer_char:
            if board[i][1] == '_':
                board[i][1] = computer_char
                return

    # |||
    for i in range(3):
        if board[0][i] == computer_char and board[1][i] == computer_char:
            if board[2][i] == '_':
                board[2][i] = computer_char
                return

        if board[1][i] == computer_char and board[2][i] == computer_char:
            if board[0][i] == '_':
                board[0][i] = computer_char
                return

        if board[0][i] == computer_char and board[2][i] == computer_char:
            if board[1][i] == '_':
                board[1][i] = computer_char
                return

    # \
    if board[0][0] == computer_char and board[1][1] == computer_char:
        if board[2][2] == '_':
            board[2][2] = computer_char
            return

    if board[0][0] == computer_char and board[2][2] == computer_char:
        if board[1][1] == '_':
            board[1][1] = computer_char
            return

    if board[2][2] == computer_char and board[1][1] == computer_char:
        if board[0][0] == '_':
            board[0][0] = computer_char
            return

    # /
    if board[0][2] == computer_char and board[1][1] == computer_char:
        if board[2][0] == '_':
            board[2][0] = computer_char
            return

    if board[2][0] == computer_char and board[1][1] == computer_char:
        if board[0][2] == '_':
            board[0][2] = computer_char
            return

    if board[0][2] == computer_char and board[2][0] == computer_char:
        if board[1][1] == '_':
            board[1][1] = computer_char
            return


    ## PREVENT LOSE
    # =
    for i in range(3):
        if board[i][0] == player_char and board[i][1] == player_char:
            if board[i][2] == '_':
                board[i][2] = computer_char
                return

        if board[i][1] == player_char and board[i][2] == player_char:
            if board[i][0] == '_':
                board[i][0] = computer_char
                return

        if board[i][0] == player_char and board[i][2] == player_char:
            if board[i][1] == '_':
                board[i][1] = computer_char
                return

    # |||
    for i in range(3):
        if board[0][i] == player_char and board[1][i] == player_char:
            if board[2][i] == '_':
                board[2][i] = computer_char
                return

        if board[1][i] == player_char and board[2][i] == player_char:
            if board[0][i] == '_':
                board[0][i] = computer_char
                return

        if board[0][i] == player_char and board[2][i] == player_char:
            if board[1][i] == '_':
                board[1][i] = computer_char
                return

    # \
    if board[0][0] == player_char and board[1][1] == player_char:
        if board[2][2] == '_':
            board[2][2] = computer_char
            return

    if board[0][0] == player_char and board[2][2] == player_char:
        if board[1][1] == '_':
            board[1][1] = computer_char
            return

    if board[2][2] == player_char and board[1][1] == player_char:
        if board[0][0] == '_':
            board[0][0] = computer_char
            return

    # /
    if board[0][2] == player_char and board[1][1] == player_char:
        if board[2][0] == '_':
            board[2][0] = computer_char
            return

    if board[2][0] == player_char and board[1][1] == player_char:
        if board[0][2] == '_':
            board[0][2] = computer_char
            return

    if board[0][2] == player_char and board[2][0] == player_char:
        if board[1][1] == '_':
            board[1][1] = computer_char
            return


    ## EARLY GAME

    # try taking corners
    good_options = [(0, 0), (0, 2), (2, 0), (2, 2)]
    rng = random.randint(0, 3)
    current_index = rng

    while True:
        board_x, board_y = good_options[current_index % 4]

        if board[board_x][board_y] == '_':
            board[board_x][board_y] = computer_char
            return
        else:
            current_index += 1
            if current_index % 4 == rng:
                break

    # look for free space
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = computer_char
                return


def choose_char():
    """ Allowing user to choose character """

    print("Choose your character: ")
    print("1 - X")
    print("2 - O")

    while True:
        choice = input()
        if choice == '1':
            return ('X', 'O')
        elif choice == '2':
            return ('O', 'X')
        else:
            print("Wrong input!")



def main():
    """ Main game loop """

    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    keys = {
        'q': (0, 0),
        'w': (0, 1),
        'e': (0, 2),
        'a': (1, 0),
        's': (1, 1),
        'd': (1, 2),
        'z': (2, 0),
        'x': (2, 1),
        'c': (2, 2),
    }


    welcome_info()
    player_char, computer_char = choose_char()
    print_board(board)

    while True:
        print("YOUR TURN")
        player_turn(board, keys, player_char)
        print_board(board)
        if check_win_condition(board, player_char):
            print("YOU WON!")
            break

        print("COMPUTER'S TURN")
        computer_turn(board, computer_char, player_char)
        print_board(board)
        if check_win_condition(board, computer_char):
            print("COMPUTER WON!")
            break

        if is_board_full(board):
            print("\n IT'S A DRAW!")
            break


if __name__ == "__main__":
    main()
