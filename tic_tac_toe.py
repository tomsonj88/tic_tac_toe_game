"""
TIC-TAC-TOE GAME
"""
import random


def welcome_intro() -> None:
    print("Welcome in TIC-TAC-TOE game")
    print("Human has O, computer has X ")


def create_board() -> list:
    board = [element + 1 for element in range(9)]

    print(board[0], '|', board[1], '|', board[2],)
    print('---------')
    print(board[3], '|', board[4], '|', board[5],)
    print('---------')
    print(board[6], '|', board[7], '|', board[8] )
    print('')

    field = [' ' for _ in range(9)]
    return field


def display_board(fields: list) -> None:
    print(fields[0], '|', fields[1], '|', fields[2], )
    print('---------')
    print(fields[3], '|', fields[4], '|', fields[5], )
    print('---------')
    print(fields[6], '|', fields[7], '|', fields[8])
    print("\n")


# def choose_first_player() -> str:
#     players = ['human', 'computer']
#     draw = random.randint(0, 1)
#     print(f"{players[draw].upper()} will start game")
#     return players[draw]

def choose_first_player(player: dict) -> str:
    choice = random.choice(list(player.keys()))
    print(f"{choice.upper()} will start game")
    return choice


def change_player(token: str) -> str:
    if token == 'O':
        token = 'X'
    else:
        token = 'O'
    return token


def choose_field(token: str) -> int:
    if token == 'O':
        field = input("Please enter number")
    else:
        field = random.randint(0, 8)
    return int(field)


def check_victory(board: list, token: str):
    winner = False
    moves_to_win = [[0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8],
                    [0, 3, 6],
                    [1, 4, 7],
                    [2, 5, 8],
                    [0, 4, 8],
                    [2, 4, 6]]

    for i in moves_to_win:
        a, b, c = i
        if board[a] == board[b] == board[c] == token:
            winner = winner or True
            display_winner(token)
            return winner
    return winner


def display_player(token: str) -> None:
    if token == 'O':
        print("Now is HUMAN turn")
    else:
        print("Now is COMPUTER turn")


def delete_from_legal_moves(moves: list, field: int) -> list:
    moves.remove(field)
    return moves


def display_winner(token: str) -> None:
    if token == 'O':
        print("The winner is HUMAN")
    else:
        print("The winner is COMPUTER")
    print("CONGRATULATIONS !!!")


def check_field() -> int:
    while True:
        field = choose_field(token)
        if field not in legal_moves:
            print("Illegal moves! Try again")
        else:
            break
    return field


def is_draw(remains_moves: list):
    if not remains_moves:
        print("It is draw")
        return True


legal_moves = [element for element in range(1, 10)]
print(legal_moves)
player = {'human': 'O', 'computer': 'X'}

welcome_intro()
active_player = choose_first_player(player)
token = player[active_player]
board_fields = create_board()
while True:
    display_board(board_fields)
    field = check_field()
    legal_moves = delete_from_legal_moves(legal_moves, field)
    board_fields[field-1] = token
    if check_victory(board_fields, token) or is_draw(legal_moves):
        display_board(board_fields)
        break
    token = change_player(token)





