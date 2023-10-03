from os import system, name
from time import sleep
from utils.tetris_classes import GameBoard, GameSpace

score = 0
time = 0
level = 0

def clear_display():
    if name == 'nt':
        system('CLS')
    else:
        system('clear')

def display_header():
    pass


def add_test_pieces():

    game_board.rows[1][3].set_piece("I")
    game_board.rows[1][4].set_piece("I")
    game_board.rows[1][5].set_piece("I")
    game_board.rows[1][6].set_piece("I")

    game_board.rows[3][1].set_piece("J")
    game_board.rows[3][2].set_piece("J")
    game_board.rows[3][3].set_piece("J")
    game_board.rows[4][3].set_piece("J")

    game_board.rows[3][6].set_piece("L")
    game_board.rows[3][7].set_piece("L")
    game_board.rows[3][8].set_piece("L")
    game_board.rows[4][6].set_piece("L")

    game_board.rows[6][4].set_piece("O")
    game_board.rows[6][5].set_piece("O")
    game_board.rows[7][4].set_piece("O")
    game_board.rows[7][5].set_piece("O")

    game_board.rows[9][2].set_piece("S")
    game_board.rows[9][3].set_piece("S")
    game_board.rows[10][1].set_piece("S")
    game_board.rows[10][2].set_piece("S")

    game_board.rows[9][6].set_piece("Z")
    game_board.rows[9][7].set_piece("Z")
    game_board.rows[10][7].set_piece("Z")
    game_board.rows[10][8].set_piece("Z")

    game_board.rows[12][4].set_piece("T")
    game_board.rows[13][4].set_piece("T")
    game_board.rows[13][5].set_piece("T")
    game_board.rows[14][4].set_piece("T")


## Set Up Game
game_board = GameBoard()
add_test_pieces()
playing = True

def refresh_display():
    clear_display()
    game_board.display_board()


while playing:
    refresh_display()
    sleep(0.03)


