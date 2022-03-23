import random

player_A = input("Player A, enter your name: ")
player_B = input("Player B, enter your name: ")
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

players = [player_A, player_B]

player_1 = random.choice(players)
players.remove(player_1)
player_2 = players[0]


print(player_1 + " is on the move with 'x'.")


def display_board():
    print(board[0] + " " + board[1] + " " + board[2])
    print(board[3] + " " + board[4] + " " + board[5])
    print(board[6] + " " + board[7] + " " + board[8])


def play_game():
    current_player = "X"
    display_board()
    while game_is_over() is False:
        move = input("Player " + current_player + ": choose the position from 1-9: ")
        move = int(move) - 1
        # TODO: Ako se unese broj izvan rangea 1-9, "list index out of range" error
        if board[move] == "_":
           board[move] = current_player
           display_board()
        else:
           print("This place is taken. Choose another number.")
           continue
        if current_player == "X":
           current_player = "0"
        else:
           current_player = "X"
    else:
        if win() is True:
            if current_player == "X":
                print(player_2 + " wins")
            elif current_player == "0":
                print(player_1 + " wins")
        else:
           print("It's a tie.")


def win():
    if board[0] == board[1] == board[2] != "_" or \
       board[3] == board[4] == board[5] != "_" or \
       board[6] == board[7] == board[8] != "_" or \
       board[0] == board[4] == board[8] != "_" or \
       board[2] == board[4] == board[6] != "_" or \
       board[2] == board[5] == board[8] != "_" or \
       board[1] == board[4] == board[7] != "_":
        return True
    else:
        return False


def tie():
    if board[0] != "_" and win() is False:
        for x in board:
            if x == "_":
                return False
        else:
            return True


def game_is_over():
    if win() is True or tie() is True:
        return True
    else:
        return False


play_game()
