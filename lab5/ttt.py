import random


board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
keys = {
    'q': (0,0),
    'w': (0,1),
    'e': (0,2),
    'a': (1,0),
    's': (1,1),
    'd': (1,2),
    'z': (2,0),
    'x': (2,1),
    'c': (2,2),
}

player_char = 'X'
computer_char = 'O'


def welcome_info():
    print("  WELCOME\n")
    print("Key bindings:")
    print(" Q | W | E")
    print(" A | S | D")
    print(" Z | X | C")
    print("\n")


def print_board():
    global board

    for i in range(3):
        for j in range(3):
            print(board[i][j] + " ", end='')
        print()
    print("\n")


def is_board_full():
    global board

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return False
    
    return True


def check_win_condition(character):
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


def player_turn():
    global player_char

    if is_board_full():
        return

    while True:
        place = input("Choose position ")

        if not place in keys:
            print("Wrong position given!")
            continue

        x, y = keys[place]

        if board[x][y] != '_':
            print("Position already taken!")
        else:
            board[x][y] = player_char
            break


def computer_turn():
    global board
    global player_char
    global computer_char

    if is_board_full():
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
        x, y = good_options[current_index % 4]

        if board[x][y] == '_':
            board[x][y] = computer_char
            return
        else:
            current_index += current_index
            if current_index % 4 == rng:
                break

    # look for free space
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = computer_char
                return


def choose_char():
    global player_char
    global computer_char

    print("Choose your character: ")
    print("1 - X")
    print("2 - O")

    while True:
        choice = input()
        if choice == '1':
            return
        elif choice == '2':
            player_char = 'O'
            computer_char = 'X'
            return
        else:
            print("Wrong input!")


def main():
    welcome_info()
    choose_char()
    print_board()

    while True:
        print("YOUR TURN")
        player_turn()
        print_board()
        if check_win_condition(player_char):
            print("YOU WON!")
            break

        print("COMPUTER'S TURN")
        computer_turn()
        print_board()
        if check_win_condition(computer_char):
            print("COMPUTER WON!")
            break

        if is_board_full():
            print("\n IT'S A DRAW!")
            break


if __name__ == "__main__":
    main()