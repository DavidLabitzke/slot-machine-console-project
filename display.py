# display.py, Controls The Way Symbols Appear On Screen
import random
from symbols import MAIN_SYMBOL_QUANTITIES, MAXI_SYMBOL_QUANTITIES, MAJOR_SYMBOL_QUANTITIES, MINOR_SYMBOL_QUANTITIES
import time

ROWS: int = 3
COLUMNS: int = 5


class Display:

    def __init__(self):
        self.main_symbols: list = [key for key, value in MAIN_SYMBOL_QUANTITIES.items() for _ in range(value)]
        self.maxi_symbols: list = [key for key, value in MAXI_SYMBOL_QUANTITIES.items() for _ in range(value)]
        self.major_symbols: list = [key for key, value in MAJOR_SYMBOL_QUANTITIES.items() for _ in range(value)]
        self.minor_symbols: list = [key for key, value in MINOR_SYMBOL_QUANTITIES.items() for _ in range(value)]
        self.jackpot_symbols: list = ["✅"]

        self.jackpot_odds = 100_000
        self.maxi_odds = 5_000
        self.major_odds = 500
        self.minor_odds = 50

        self.promotional_message = None

        self.board_compared_list: list = []
        self.board_displayed_list: list = []

    def pick_board_to_use(self):
        check_jackpot = random.randint(0, self.jackpot_odds)
        check_maxi = random.randint(0, self.maxi_odds)
        check_major = random.randint(0, self.major_odds)
        check_minor = random.randint(0, self.minor_odds)
        if check_jackpot == 1:
            return self.jackpot_symbols
        elif check_maxi == 1:
            return self.maxi_symbols
        elif check_major == 1:
            return self.major_symbols
        elif check_minor == 1:
            return self.minor_symbols
        else:
            return self.main_symbols

    def change_promotional_message(self, symbols):
        if symbols == self.jackpot_symbols:
            self.promotional_message = "JACKPOT!!!\n"
        if symbols == self.maxi_symbols:
            self.promotional_message = "MAXI WINNINGS POSSIBLE!!!"
        if symbols == self.major_symbols:
            self.promotional_message = "MAJOR WINNINGS POSSIBLE!!!"
        if symbols == self.minor_symbols:
            self.promotional_message = "MINOR WINNINGS POSSIBLE!!!"

    def create_boards_lists(self):
        """Creates the values stored in board_compared_list and board_displayed_list.
        board_compared_list is used to evaluate wins.
        board_displayed_list is used to create the board displayed to the user"""
        symbols_to_use = self.pick_board_to_use()
        self.change_promotional_message(symbols_to_use)

        for i in range(COLUMNS):
            new_row: list = [random.choice(symbols_to_use) for _ in range(ROWS)]
            self.board_compared_list.append(new_row)
        self.board_displayed_list = [[self.board_compared_list[j][i] for j in range(COLUMNS)] for i in range(ROWS)]

    def create_board_display(self):
        """Creates the board to be displayed onto the console from board_displayed_list, and prints it"""
        self.create_boards_lists()
        board_display: str = ""
        for row in self.board_displayed_list:
            board_display += "|"
            for i in range(COLUMNS):
                board_display += row[i] + "\ufe0f"
                board_display += "|"
            board_display += "\n"

        if self.promotional_message is not None:
            print(self.promotional_message)
            time.sleep(5)
        if self.promotional_message != "JACKPOT!!!\n":
            print("Good Luck \n")

        for char in board_display:
            print(char, end="")
            time.sleep(0.05)
        print("\n")

    def reset_boards(self):
        """Resets the values of the board lists, so they can be refilled with new values"""
        self.board_compared_list = []
        self.board_displayed_list = []
        self.promotional_message = None
