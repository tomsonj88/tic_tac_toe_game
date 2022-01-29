"""
TIC-TAC-TOE GAME
"""
import random


def welcome_intro():
    print("Welcome in TIC-TAC-TOE game")
    print("Human has O, computer has X ")


def create_board():
    board = [element + 1 for element in range(9)]

    print(board[0], '|', board[1], '|', board[2],)
    print('---------')
    print(board[3], '|', board[4], '|', board[5],)
    print('---------')
    print(board[6], '|', board[7], '|', board[8] )
    print('')

    field = [' ' for _ in range(9)]
    return field


def display_board(field):
    print(field[0], '|', field[1], '|', field[2], )
    print('---------')
    print(field[3], '|', field[4], '|', field[5], )
    print('---------')
    print(field[6], '|', field[7], '|', field[8])


def choose_first_player():
    players = ['human', 'computer']
    draw = random.randint(0, 1)
    print(f"{players[draw].upper()} will start game")
    return players[draw]


def give_token(player):
    if player == 'human':
        token = 'O'
    else:
        token = 'X'
    return token


def change_player(token):
    if token == 'O':
        token = 'X'
    else:
        token = 'O'
    return token


def choose_field(token):
    if token == 'O':
        field = input("Please enter number")
    else:
        field = random.randint(0, 8)
    return int(field)


def check_victory(board, token):
    winner = True
    moves_to_win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 7]]

    for i in moves_to_win:
        a, b, c = i
        if board[a] == board[b] == board[c] == token:
            print("victory")
            winner = winner and True
            return winner
        else:
            winner = winner and False
    return winner


def display_player(token):
    if token == 'O':
        print("Now is HUMAN turn")
    else:
        print("Now is COMPUTER turn")


def delete_from_legal_move(moves, field):
    moves.remove(field)
    return moves


def display_winner(token):
    if token == 'O':
        print("The winner is HUMAN")
    else:
        print("The winner is COMPUTER")
    print("CONGRATULATIONS !!!")


legal_moves = [element for element in range(1, 10)]
print(legal_moves)
field = 0

welcome_intro()
player = choose_first_player()
token = give_token(player)
board_fields = create_board()
while True:
    display_board(board_fields)
    while field not in legal_moves:
        field = choose_field(token)
        print("Illegal moves! Try again")
    board_fields[field-1] = token
    if check_victory(board_fields, token):
        print(f"The winner is {token}")
        break
    legal_moves = delete_from_legal_move(legal_moves, field)
    token = change_player(token)





