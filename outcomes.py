# outcomes.py, handles any outputs to the user
from line_combos_configurations import LINE_COMBOS_CONFIGURATIONS
from line_combos_outcomes import LINE_COMBOS_OUTCOMES
from symbols import SYMBOL_PAYOUTS
import time

FOUR_LINE_BONUS: int = 4
FIVE_LINE_BONUS: int = 10

# Used for diagnosing pay out percentage
payout_numerator = 0
payout_denominator = 0
DIAGNOSING_PASSCODE = "Test"


class Outcomes:

    def __init__(self, num_lines_bid_on: int, amount_bid: int, board_to_compare: list, diagnosing: str):
        self.num_lines_bid_on: int = num_lines_bid_on
        self.bid_per_line: int = amount_bid
        self.board_to_compare: list = board_to_compare
        self.total_win: int = 0
        self.diagnosing = (diagnosing == DIAGNOSING_PASSCODE)

    def create_lines(self):
        """Fills LINE_COMBOS_OUTCOMES with the values of each corresponding line on the board"""
        for i in range(self.num_lines_bid_on):
            current_line: int = i + 1
            current_line_outcome: str = ""
            for index, row in enumerate(self.board_to_compare):
                item_to_put: str = row[LINE_COMBOS_CONFIGURATIONS[current_line][index]]
                current_line_outcome += item_to_put
            LINE_COMBOS_OUTCOMES[current_line] = current_line_outcome

    def calculate_earning_per_line(self, total_symbols_same, value_to_compare) -> int:
        """Calculate's each line's earning based on the number of matching symbols"""
        line_win = 0
        base_payout = self.bid_per_line * SYMBOL_PAYOUTS[value_to_compare]
        match total_symbols_same:
            case 3:
                line_win += base_payout
            case 4:
                line_win: int = base_payout * FOUR_LINE_BONUS
            case 5:
                line_win: int = base_payout * FIVE_LINE_BONUS
        return line_win

    @staticmethod
    def calculate_total_same(items_being_compared, value_to_compare) -> int:
        """Checks how many symbols within a line match up"""
        total_symbols_same = 0
        for symbol in items_being_compared:
            if symbol != value_to_compare:
                break
            total_symbols_same += 1
        return total_symbols_same

    def sum_each_line_winnings(self) -> int:
        """Checks each of the outcome to see if it has won,
        accumulates the win across each line,
        and returns the cumulative win"""
        total_win: int = 0
        for key, value in LINE_COMBOS_OUTCOMES.items():
            if value is not None:
                value_to_compare: str = value[0]
                value_to_display: str = value_to_compare + "\ufe0f"
                total_symbols_same: int = self.calculate_total_same(items_being_compared=value,
                                                                    value_to_compare=value_to_compare)

                line_earning = self.calculate_earning_per_line(total_symbols_same, value_to_compare)
                total_win += line_earning
                if total_symbols_same >= 3:
                    time.sleep(0.25)
                    print(f"You've won ${line_earning / 100: .2f} with {total_symbols_same} "
                          f"{value_to_display}'s on line {key}")

        return total_win

    def display_total_winnings(self) -> int:
        """Calls sum_each_line_winnings to get the total win, display the appropriate message,
        and return total win"""
        global payout_numerator, payout_denominator
        total_win: int = self.sum_each_line_winnings()

        self.total_win += total_win
        time.sleep(1)
        payout_denominator += 1
        if self.total_win == 0:
            print("Better Luck Next Time")
        else:
            print(f"Your total payout is ${self.total_win / 100: .2f}")
            payout_numerator += 1

        if self.diagnosing:
            print(f"This machine pays out {payout_numerator}/{payout_denominator} times")
        return self.total_win

    def reset_values(self):
        """Resets the total_win and LINE_COMBOS_OUTCOMES to their default values"""
        for key, value in LINE_COMBOS_OUTCOMES.items():
            LINE_COMBOS_OUTCOMES[key] = None

        self.total_win = 0
