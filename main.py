# Main.py, Runs Program
import time
from display import Display
from user import User
from outcomes import Outcomes
from rules import hear_rules
from keyboard_controls import disable_keyboard, enable_keyboard


def main():
    """Runs The Game"""
    display = Display()
    user = User()
    print("Welcome To My Slot Machine!!!")
    hear_rules()
    user.get_deposit()
    user.get_lines()
    user.get_bid_per_line()
    user.calculate_new_bid_total(per_line=user.bid_per_line, num_lines=user.num_lines_bid_on)
    while user.is_playing:
        if not user.bid_total <= user.balance:
            print("Insufficient funds!")
            print("Would you like to add more money, or change your bid?")
            deposit_more = input("Type 'y' to add money, anything else to adjust bid: ")
            if deposit_more.lower() == "y":
                user.get_deposit()
            user.get_lines()
            user.get_bid_per_line()
            user.calculate_new_bid_total(per_line=user.bid_per_line, num_lines=user.num_lines_bid_on)
        else:
            print("\n")
            user.deduct_bet_from_balance()
            display.create_board_display()
            reward_calculator = Outcomes(user.num_lines_bid_on, user.bid_per_line, display.board_compared_list)
            reward_calculator.create_lines()
            user.balance += reward_calculator.display_total_winnings()
            print(f"Your balance now is ${user.balance / 100: .2f}\n")
            disable_keyboard()
            time.sleep(2)
            enable_keyboard()
            if user.continue_playing():
                print("\nDo you want to add more funds?")
                user_wants_add_money = input("Type 'y' to add funds, anything else to continue playing: ")
                if user_wants_add_money.lower() == "y":
                    user.get_deposit()
                print("\nDo you want to keep your bets the same?")
                user_wants_same_bid = input("Type 'n' to change your bid, anything else to continue playing: ")
                if user_wants_same_bid.lower() == "n":
                    user.get_lines()
                    user.get_bid_per_line()
                    user.calculate_new_bid_total(per_line=user.bid_per_line, num_lines=user.num_lines_bid_on)
                display.reset_boards()
                print("\n")


if __name__ == "__main__":
    main()
