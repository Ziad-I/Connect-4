from PIL import ImageGrab
import pyautogui
import numpy as np

# YOU MAY NEED TO CHANGE THESE VALUES BASED ON YOUR SCREEN SIZE
# 780 width
# 675 height

#! Hamza's Values
LEFT = 431
TOP = 190
RIGHT = 934
BOTTOM = 619
START_CORD = (39, 34)
STEP = 71

#! Ziad's Values
# LEFT = 591
# TOP = 256
# RIGHT = 1308
# BOTTOM = 871
# START_CORD = (50, 50)
# STEP = 100

EMPTY = 0
RED = 1
BLUE = 2


class Board:
    def __init__(self) -> None:
        self.board = [[EMPTY for i in range(7)] for j in range(6)]
        # self.board = np.full((6, 7), EMPTY, dtype=int)

    def print_grid(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY:
                    print("*", end=" \t")
                elif grid[i][j] == RED:
                    print("R", end=" \t")
                elif grid[i][j] == BLUE:
                    print("B", end=" \t")
            print("\n")

    def _convert_grid_to_color(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == (255, 255, 255):
                    grid[i][j] = EMPTY
                elif grid[i][j][0] > 200:
                    grid[i][j] = RED
                elif grid[i][j][0] > 50:
                    grid[i][j] = BLUE
        return grid

    def _get_grid_cordinates(self):
        startCord = START_CORD
        cordArr = []
        for i in range(0, 7):
            for j in range(0, 6):
                x = startCord[0] + i * STEP
                y = startCord[1] + j * STEP
                cordArr.append((x, y))
        return cordArr

    def _get_column_cordinates(self):
        startCord = START_CORD
        cordArr = []
        # 7
        # 6
        for i in range(0, 7):
            x = startCord[0] + i * STEP
            cordArr.append((x, startCord[1]))
        return cordArr

    def _transpose_grid(self, grid):
        return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

    def _capture_image(self):
        image = ImageGrab.grab()
        cropedImage = image.crop((LEFT, TOP, RIGHT, BOTTOM))
        return cropedImage

    def _convert_image_to_grid(self, image):
        pixels = [[] for i in range(7)]
        i = 0
        for index, cord in enumerate(self._get_grid_cordinates()):
            pixel = image.getpixel(cord)
            if index % 6 == 0 and index != 0:
                i += 1
            pixels[i].append(pixel)
        return pixels

    def _get_grid(self):
        cropedImage = self._capture_image()
        # cropedImage.show()
        pixels = self._convert_image_to_grid(cropedImage)
        # cropedImage.show()
        grid = self._transpose_grid(pixels)
        return grid

    def _check_if_game_end(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY and self.board[i][j] != EMPTY:
                    return True
        return False

    def get_game_grid(self):
        game_grid = self._get_grid()
        new_grid = self._convert_grid_to_color(game_grid)
        is_game_end = self._check_if_game_end(new_grid)
        self.board = new_grid
        return (self.board, is_game_end)

    def select_column(self, column):
        pyautogui.click(
            self._get_column_cordinates()[column][0] + LEFT,
            self._get_column_cordinates()[column][1] + TOP,
        )
