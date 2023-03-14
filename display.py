# display.py, Controls The Way Symbols Appear On Screen
import random
from symbols import SYMBOL_QUANTITIES

ROWS = 3
COLUMNS = 5


class Display:

    def __init__(self):
        self.symbols: list = [key for key, value in SYMBOL_QUANTITIES.items() for _ in range(value)]
        self.board_compared_list: list = []
        self.board_displayed_list: list = []

    def create_boards_lists(self):
        for i in range(COLUMNS):
            new_row = [random.choice(self.symbols) for _ in range(ROWS)]
            self.board_compared_list.append(new_row)
        self.board_displayed_list = [[self.board_compared_list[j][i] for j in range(COLUMNS)] for i in range(ROWS)]

    def create_board_display(self):
        self.create_boards_lists()
        board_display = ""
        for column in self.board_displayed_list:
            board_display += "|"
            for i in range(COLUMNS):
                board_display += column[i] + "\ufe0f"
                board_display += "|"
            board_display += "\n"

        print(board_display)

    def reset_board(self):
        self.board_compared_list = []
        self.board_displayed_list = []
