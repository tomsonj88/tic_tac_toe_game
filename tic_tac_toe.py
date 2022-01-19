"""
TIC-TAC-TOE GAME
"""
import random


def welcome_intro():
    print("Welcome in TIC-TAC-TOE game")
    print("Human has O, computer has X ")


def display_board(board):

  print(board[0], '|', board[1], '|', board[2],)
  print('---------')
  print(board[3], '|', board[4], '|', board[5],)
  print('---------')
  print(board[6], '|', board[7], '|', board[8], )


def change_player(player):
    if player == 'O':
       player = 'X'
    else:
        player = 'O'
    return player


def choose_field(player):
    if player == 'O':
        field = input("Please enter number")
    else:
        field = random.randint(0, 8)
    return int(field)


def check_victory(board):
    if (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[7]):
        print("dupa")
        return True



def display_player(player):
    if player == 'O':
        print("Now is HUMAN turn")
    else:
        print("Now is COMPUTER turn")


def check_choice(moves, field):
    if field not in moves:
        moves.append(field)
        return True
    else:
        print("Duplicate field! Please choose again")
        return False


def display_winner(player):
    if player == 'O':
        print("The winner is HUMAN")
    else:
        print("The winner is COMPUTER")
    print("CONGRATULATIONS !!!")


turn = 'O'
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
moves = []

welcome_intro()
while True:
    display_board(board)
    if len(moves) >= 9:
        print("Game over! No more moves on the table")
        break
    display_player(turn)
    field = choose_field(turn)
    if not check_choice(moves, field):
        continue
    board[field-1] = turn
    if check_victory(board):
        display_board(board)
        display_winner(turn)
        break
    turn = change_player(turn)






