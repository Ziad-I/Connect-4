from board import Board
import time
import copy

# GAME LINK
# http://kevinshannon.com/connect4/
from algorithm import *


def main():
    board = Board()

    time.sleep(4)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()
        
        # FOR DEBUG PURPOSES
        board.print_grid(game_board)
        print("\n")
        reversed_board = copy.deepcopy(game_board)
        reversed_board = reversed_board[::-1]
        # YOUR CODE GOES HERE
        (column, value) = minimax(reversed_board, 6, N_INF, INF, True)

        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the followi+ng function to select a column
        # column = random.randint(0, 6)
        board.select_column(column)
        if game_end:
                print("gg")
        time.sleep(2)

if __name__ == "__main__":
    main()
