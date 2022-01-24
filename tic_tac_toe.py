"""
TIC-TAC-TOE GAME
"""
import random


def welcome_intro():
    print("Welcome in TIC-TAC-TOE game")
    print("Human has O, computer has X ")


def create_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(board[0], '|', board[1], '|', board[2],)
    print('---------')
    print(board[3], '|', board[4], '|', board[5],)
    print('---------')
    print(board[6], '|', board[7], '|', board[8] )
    print('')


def display_board(board = ['','','','','','','','','']):
    print(board[0], '|', board[1], '|', board[2],)
    print('---------')
    print(board[3], '|', board[4], '|', board[5],)
    print('---------')
    print(board[6], '|', board[7], '|', board[8] )


def choose_first_player():
    players = ['human', 'computer']
    draw = random.randint(0, 1)
    print(f"{players[draw].upper()} will start game")
    return players[draw]


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


def check_victory(board, player):
    winner = True
    moves_to_win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 7]]

    for i in moves_to_win:
        a, b, c = i
        if board[a] == board[b] == board[c]:
            print("victory")
            winner = winner and True
            return winner
        else:
            winner = winner and False
            return winner


def display_player(player):
    if player == 'O':
        print("Now is HUMAN turn")
    else:
        print("Now is COMPUTER turn")


def legal_moves(moves, field):
    for element in moves:
        if element == field:
            moves.remove(element)
    return moves


def display_winner(player):
    if player == 'O':
        print("The winner is HUMAN")
    else:
        print("The winner is COMPUTER")
    print("CONGRATULATIONS !!!")


turn = 'O'
moves = []
board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# welcome_intro()
# choose_first_player()
create_board()
display_board()





