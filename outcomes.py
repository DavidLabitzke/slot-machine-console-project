# outcomes.py, handles any outputs to the user
from line_combos_configurations import LINE_COMBOS_CONFIGURATIONS
from line_combos_outcomes import LINE_COMBOS_OUTCOMES
from symbols import SYMBOL_VALUES

FOUR_LINE_BONUS: int = 4
FIVE_LINE_BONUS: int = 10


class Outcomes:

    def __init__(self, num_lines_bid_on: int, amount_bid: int, board_to_compare):
        self.num_lines_bid_on: int = num_lines_bid_on
        self.bid_per_line: int = amount_bid
        self.board_to_compare = board_to_compare
        self.total_win: int = 0

    def create_lines(self):
        for i in range(self.num_lines_bid_on):
            current_line = i + 1
            current_line_outcome = ""
            for index, row in enumerate(self.board_to_compare):
                item_to_put = row[LINE_COMBOS_CONFIGURATIONS[current_line][index]]
                current_line_outcome += item_to_put
            LINE_COMBOS_OUTCOMES[current_line] = current_line_outcome

    def check_if_winner(self) -> int:
        total_win: int = 0
        for key, value in LINE_COMBOS_OUTCOMES.items():
            if value is not None:
                current_line_num = key
                items_being_compared = value
                value_to_compare = value[0]
                value_to_display = value_to_compare + "\ufe0f"
                total_symbols_same = 0

                for symbol in items_being_compared:
                    if symbol != value_to_compare:
                        break
                    total_symbols_same += 1

                match total_symbols_same:
                    case 3:
                        amount_won = self.bid_per_line * SYMBOL_VALUES[value_to_compare]
                        total_win += amount_won
                        print(f"You've won ${amount_won / 100: .2f} with {total_symbols_same} "
                              f"{value_to_display}'s on line {current_line_num}")
                    case 4:
                        amount_won = self.bid_per_line * SYMBOL_VALUES[value_to_compare] * FOUR_LINE_BONUS
                        total_win += amount_won
                        print(f"You've won ${amount_won / 100: .2f} with {total_symbols_same} "
                              f"{value_to_display}'s on line {current_line_num}")
                    case 5:
                        amount_won = self.bid_per_line * SYMBOL_VALUES[value_to_compare] * FIVE_LINE_BONUS
                        total_win += amount_won
                        print(f"You've won ${amount_won / 100: .2f} with {total_symbols_same} "
                              f"{value_to_display}'s on line {current_line_num}")

        self.total_win += total_win

        if self.total_win == 0:
            print("Better Luck Next Time")
        else:
            print(f"Your total payout is ${self.total_win / 100: .2f}")
        return self.total_win

    def reset_values(self):
        for key, value in LINE_COMBOS_OUTCOMES.items():
            LINE_COMBOS_OUTCOMES[key] = None

        self.total_win = 0
