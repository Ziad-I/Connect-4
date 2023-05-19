from board import Board
import time
import copy

import numpy as np

# GAME LINK
# http://kevinshannon.com/connect4/
from Algorithm import *


def start(difficultly, algorithm):
    board = Board()

    time.sleep(4)
    start = time.time()
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()
        
        # FOR DEBUG PURPOSES
        board.print_grid(game_board)
        print("\n")
        reversed_board = copy.deepcopy(game_board)
        reversed_board = reversed_board[::-1]   
        reversed_board = np.array(reversed_board, dtype = int)
        # YOUR CODE GOES HERE
        if algorithm == 1:
            (column, value) = minimax(reversed_board, difficultly*2, True)
        else:
            (column, value) = alpha_beta(reversed_board, difficultly*2, N_INF, INF, True)

        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        # column = random.randint(0, 6)
        board.select_column(column)
        time.sleep(2)

    end = time.time()
    print(end - start)
