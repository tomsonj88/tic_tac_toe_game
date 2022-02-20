"""
TIC-TAC-TOE GAME
"""
import random
from typing import Union


class Board:
    # show_demo_board
    # display board

    def __init__(self, fields):
        self.fields = fields

    @staticmethod
    def show_demo_board() -> None:
        """
        Function show demo board for tic-tac-toe game
        :return: None
        """
        board = list(range(1, 10))

        print(board[0], '|', board[1], '|', board[2], )
        print('---------')
        print(board[3], '|', board[4], '|', board[5], )
        print('---------')
        print(board[6], '|', board[7], '|', board[8])
        print('')

    def display_board(self) -> None:
        """
        Methods display board with current moves
        :return: None
        """
        print(self.fields[0], '|', self.fields[1], '|', self.fields[2], )
        print('---------')
        print(self.fields[3], '|', self.fields[4], '|', self.fields[5], )
        print('---------')
        print(self.fields[6], '|', self.fields[7], '|', self.fields[8] )
        print("\n")


class Game:
    def __init__(self, player):
        self.player = player

    #welcome_intro
    @staticmethod
    def welcome_intro() -> None:
        """
        Function displays welcome intro with instructions
        :return: None
        """
        print("Welcome in TIC-TAC-TOE game")
        print("Human has O, computer has X ")


    #choose_first_player
    def choose_first_player(self) -> str:
        choice = random.choice(list(self.player.keys()))
        print(f"{choice.upper()} will start game")
        return choice

    #change player
    @staticmethod
    def change_player(token: str) -> str:
        if token == 'O':
            token = 'X'
        else:
            token = 'O'
        return token

    #check_victory
    @staticmethod
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
                winner = True
                return winner
        return winner

    #display_player
    @staticmethod
    def display_player(turn: str) -> None:
        if turn == 'O':
            print("Now is HUMAN turn")
        else:
            print("Now is COMPUTER turn")

    #delete_from_legal_moves
    #display_winner
    #check_field
    #is_draw



class Player(Game):
    #choose_field
    # display winner
    pass


def choose_field(token: str) -> int:
    if token == 'O':
        field = input("Please enter number")
    else:
        field = computer_turn(board_fields)
    return int(field)


def display_player(turn: str) -> None:
    if turn == 'O':
        print("Now is HUMAN turn")
    else:
        print("Now is COMPUTER turn")


def delete_from_legal_moves(moves: list, field: int) -> list:
    moves.remove(field)
    return moves


def display_winner(turn: str) -> None:
    if turn == 'O':
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


def is_draw(remains_moves: list) -> Union[None, bool]:
    if not remains_moves:
        return True


def computer_turn(board_fields, token='X'):
    board = board_fields[:]
    counter = 0

    while counter < 2:
        for element in range(len(board)):
            if board[element] == ' ':
                board[element] = token
                if game.check_victory(board, token):
                    return element + 1
                board[element] = ' '
        token = game.change_player(token)
        counter += 1
    return choose_computer_best_move(board)


def choose_computer_best_move(board_fields) -> Union[None, int]:
    best_moves = [5, 1, 3, 7, 9, 2, 4, 6, 8]

    for element in best_moves:
        if board_fields[element-1] == ' ':
            return element

board_fields = [' ' for _ in range(9)]
player = {'human': 'O', 'computer': 'X'}
legal_moves = list(range(1, 10))

game_field = Board(board_fields)
game = Game(player)


game.welcome_intro()

active_player = game.choose_first_player()
token = player[active_player]


game_field.show_demo_board()

while True:
    game_field.display_board()
    field = check_field()
    legal_moves = delete_from_legal_moves(legal_moves, field)
    board_fields[field-1] = token
    if game.check_victory(board_fields, token):
        display_winner(token)
        break
    elif is_draw(legal_moves):
        print("It is draw")
        break
    # token = change_player(token)
    token = game.change_player(token)
game_field.display_board()
