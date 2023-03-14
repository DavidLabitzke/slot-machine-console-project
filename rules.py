# rules.py, displays the prompt for the rules of the game
import time
from user import NUM_LINES_POSSIBLE, BIDS_POSSIBLE_PER_LINE
from display import ROWS, COLUMNS
from symbols import SYMBOL_VALUES
from outcomes import FIVE_LINE_BONUS, FOUR_LINE_BONUS
from line_combos_configurations import LINE_COMBOS_CONFIGURATIONS


def hear_rules():
    print("Would you like to hear the rules?")
    response = input("Hit 'y' to hear the rules. Anything else to continue: ")
    if not response == "y":
        return
    print(f"This slot machine's board consists of {ROWS} rows and {COLUMNS} columns")
    print(f"The objective is to match 3 or more symbols in one of up to {NUM_LINES_POSSIBLE[-1]} lines")
    time.sleep(10)
    print(f"These are all {NUM_LINES_POSSIBLE[-1]} possible lines to bid on")
    time.sleep(2)
    for i in range(len(LINE_COMBOS_CONFIGURATIONS)):
        print(create_lines_board(i + 1, LINE_COMBOS_CONFIGURATIONS[i + 1]))
        time.sleep(2)
    print(f"You can bid between {BIDS_POSSIBLE_PER_LINE[0]} to {BIDS_POSSIBLE_PER_LINE[-1]} pennies per line")
    print(f"Additionally, there are {len(SYMBOL_VALUES)} possible symbols to match up")
    print("Each symbol awards you a different amount of pennies per penny bid on that line,"
          "if the first 3 symbols of a line (starting left to right) are the same")
    print(f"If 4 of those symbol fall in a row, the payout will be multiplied by {FOUR_LINE_BONUS}")
    print(f"If all 5 symbols within a line are the same, the payout will be multiplied by {FIVE_LINE_BONUS}")
    time.sleep(10)
    print(f"These are all {len(SYMBOL_VALUES)} symbols, with their values per 3, 4, and 5 in a row respectively\n")
    for key, value in SYMBOL_VALUES.items():
        print(key + "\ufe0f")
        print(f"First 3: {value}")
        print(f"First 4: {value * FOUR_LINE_BONUS}")
        print(f"All 5: {value * FIVE_LINE_BONUS}")
        print("\n")
        time.sleep(3)
    print("That should cover just about everything. Good luck and happy playing!")


def create_lines_board(line_num: int, line_list: list):
    game_board = [[" " for _ in range(ROWS)] for _ in range(COLUMNS)]
    for index, game_row in enumerate(game_board):
        game_row[line_list[index]] = "x"
    board_display_list = [[game_board[j][i] for j in range(COLUMNS)] for i in range(ROWS)]
    board_display = ""
    for column in board_display_list:
        board_display += "|"
        for i in range(COLUMNS):
            board_display += column[i]
            board_display += "|"
        board_display += "\n"
    return f"{line_num}\n{board_display} "
