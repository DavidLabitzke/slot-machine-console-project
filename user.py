# user.py, handles any inputs from the user
NUM_LINES_POSSIBLE: list = [5, 10, 15, 20, 25]
BIDS_POSSIBLE_PER_LINE: list = [1, 2, 5, 10, 20]


class User:

    def __init__(self):
        self.balance: int = 0
        self.num_lines_bid_on: int = 5
        self.bid_per_line: int = 1
        self.bid_total: int = self.num_lines_bid_on * self.bid_per_line
        self.is_playing: bool = True

    def get_deposit(self):
        """Script that plays at the beginning to capture the user's initial deposit"""
        while True:
            deposit_amount = input("How Much Would You Like To Deposit? (This machine only accepts bills. No coins) $")
            try:
                deposit_amount = int(deposit_amount)
            except ValueError:
                print("Invalid Entry! Try Again!")
            else:
                if deposit_amount <= 0:
                    print("Insufficient Funds! Please Insert A Valid Amount Of Money!")
                else:
                    self.balance += deposit_amount * 100
                    break

    def get_lines(self):
        """Script that runs to capture the number of lines the user wants to bid on"""
        while True:
            possibilities: str = str(NUM_LINES_POSSIBLE)[1:-1]
            error_message: str = f"Please type in either {possibilities}"
            num_of_lines = input(f"How Many Lines Would You Like To Bid On? ({possibilities}): ")
            try:
                num_of_lines = int(num_of_lines)
            except ValueError:
                print(error_message)
            else:
                if num_of_lines not in NUM_LINES_POSSIBLE:
                    print(error_message)
                else:
                    self.num_lines_bid_on = num_of_lines
                    break

    def get_bid_per_line(self):
        """Script that runs to capture the amount bid per line"""
        while True:
            bid_possibilities: str = str(BIDS_POSSIBLE_PER_LINE)[1:-1]
            error_message: str = f"Please Type In Either {bid_possibilities}"
            bid_per_line = input(f"How Many Pennies Would You Like To Bid Per Line? ({bid_possibilities}): ")
            try:
                bid_per_line = int(bid_per_line)
            except ValueError:
                print(error_message)
            else:
                if bid_per_line not in BIDS_POSSIBLE_PER_LINE:
                    print(error_message)
                else:
                    self.bid_per_line = bid_per_line
                    break

    def calculate_new_bid_total(self, per_line, num_lines):
        """Changes the self.bid_total"""
        self.bid_total = per_line * num_lines

    def deduct_bet_from_balance(self):
        """Calculates the bid total and subtracts that from the balance"""
        self.bid_total = self.num_lines_bid_on * self.bid_per_line
        self.balance -= self.bid_total
        print(f"You have ${self.balance / 100: .2f} remaining")

    def continue_playing(self) -> bool:
        """Script that plays after each spin, asking if the user wants to continue playing"""
        print("Would you like to keep playing?")
        keep_playing = input("Type 'n' to stop playing, anything else to continue: ")
        if keep_playing.lower() == "n":
            self.is_playing = False
            print(f"Thanks for playing. Your total payout is ${self.balance / 100: .2f}")
        return self.is_playing
