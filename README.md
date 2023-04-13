# slot-machine-console-project

# My First Slot Machine Project in Python

This is a simple, terminal based slot machine project, written entirely in Python. 
The goal of the game is to match 3 or more symbols in up to 25 lines the machine currently offers. 
The game board features 3 rows and 5 columns. 
This is a penny machine, meaning that bets are placed in pennies per line. The player can bid between 1-20 pennies per line
There are 16 different emojis that can appear, which can be matched.
Each emoji returns a different amount if 3 are matched on a line. 
If 4 are matched, the reward is multiplied by 4
If 5 are matched, the reward is multiplied by 10
These are all 16 emojis, with the reward given in pennies
✅ - 10,000 
♦ - 5,000
♥ - 4,000
♣ - 3,000
♠ - 2,000
☯ - 1,000 
🔴 - 500
🔵 - 250 
⚫ - 125
🍒 - 100
🍉 - 75
🍊 - 50
🍇 - 30
🍋 - 20 
🍈 - 10
🍏 - 5

This should give a general overview of the basic game mechanics and rules. 
Next I want to briefly explain the role of each file, as well as discuss future plans for this projects

# line_combos_configurations.py

This stores 1 dictionary of the line number as the key, and the value is a list of integers, which represent which value in a row is part of that line.
The way this program reads a line is by examining all 5 columns and indexing which item in that column is a part of that row. 
Since there are 3 items per column, the indexes are either 0, 1, or 2. 
For example, line 1 runs through the middle of the board, so the list associated with it is [1, 1, 1, 1, 1]

# line_combos_outcomes.py

This stores 1 dictionary of the line number as the key, and to start each value is None. 
The reason for this is because this dictionary stores the outcome of each line, so that it can be examined later. 
The stored value is a string of emojis, which is compared in a separate file

# symbols.py

This stores 2 dictionaries, one called SYMBOL_VALUES and the other SYMBOL_QUANTITIES
For each dictionary, the keys are all 16 emojis. 
SYMBOL_VALUES represents the payout for each emoji, as listed above
SYMBOL_QUANTITIES represents the number of times that emoji will be stored in a list, for the program to later pick from. 
The ✅ emoji is only stored 4 times in that list, while the 🍏 is stored 200 times. 
In total, there are 1500 symbols being stored in the list for the program to choose from. 

# rules.py

This is simply an optional script that may be played by the user if they so choose. 
There is a function in the user.py file, which is responsible for activating this script. 
If activated, it will explain the rules of the slot machine to the user

# user.py

This stores the User class, which is responsible for the majority of inputs the user provides.

## Global Variables

This also stores 2 global variables.   
NUM_LINES_POSSIBLE - list of the number of lines a user can choose to bid on. It has 5 values, ranging from 5 to 25  
BIDS_POSSIBLE_PER_LINE - list of the number of pennies a user can bid on per line. It has 5 values, ranging from 1 to 20  

## Attributes

A User object is created in the main.py file, and is initialized with balance, num_lines_bid_on, bid_per_line, bid_total, and is_playing attributes.  
Balance - the amount of money the user has to play with, stored as an int (representing the number of pennies the user has)  
num_lines_bid_on - the number of lines the user wants to bid on  
bid_per_line - the number of pennies being bid by the user per line  
bid_total - calculated by multiplying num_lines_bid_on by bid_per_line. This is the total amount the user is waging per spin  
is_playing - a boolean, set to True, which is responsible for controlling the flow of the game  

## Methods

The User class has 8 methods.   
1. get_deposit - captures how much money the user wants to enter into the machine to begin with  
2. get_lines - captures how many lines the user wants to bid on  
3. get_bid_per_line - captures the user's bid per line  
4. calculate_new_bid_total - called to adjust the user's bid total after the previous 2 methods have been called. Takes the per line bid and the number of lines bid on as parameters  
5. deduct_bid_from_total - subtracts the bid total from the user's balance  
6. continue_playing - displays a script asking if the user wants to continue playing. If they type 'n', the is_playing variable will switch to False, ending the game  
7. double_check_deposit - called if the user does not want to change their bid when they haven't got enough money. It will urge the user to add more funds, otherwise the game ends  
8. double_check_bid - called if the user does not have enough money to place the current bid. It gives the user the option to either adjust their bid, or add more money  

# display.py

This stores the Display class, which is used for storing data about the gameboard. 

## Global Variables

This also stores 2 global variables  
ROWS - the number of rows on the gameboard  
COLUMNS - the number of columns on the gameboard  

## Attributes

A Display object is created in the main.py file, and is initialized with symbols, board_compared, and board_displayed attributes    
symbols - stores a list of all the possible symbols to choose from, per the number of times specified in the SYMBOL_QUANTITIES dictionary. This is achieved by a list comprehension    
board_compared_list - stores a list of 5 lists, which represents each of the 5 columns of the gameboard. Initially an empty list, this is used to determine if any symbols match on a line and to calculate payouts    
board_displayed_list - stores a list of 3 lists, which represents each of the 3 rows of the gameboard. Initially an empty list, this is used to create the board that is displayed to the user   

## Methods

The Display class has 3 methods.   
1. create_board_lists - The random module is used to randomly select emojis from the symbols list, which first creates the board_compared list. Afterwards, a list comprehension is used to create the board_display list  
2. create_board_display - Calls the create_board_lists method, then uses the board_displayed list to print the board to the console for the user
3. reset_boards - resets the board_compared and board_displayed to its inital value  

# outcomes.py

This stores the Outcomes class, which is used to determine any payouts to the user  

## Global Variables

This also stores 2 global variables  
FOUR_LINE_BONUS - an int which is multiplied to a line's payout if there are 4 matching symbols  
FIVE_LINE_BONUS - an int which is multiplied to a line's payout if there are 5 matching symbols  

## Attributes

An Outcomes object is created in the main.py file once the user's bid per line, number of lines bid on are captured, as well as the board_compared in the display is created.   
These are all required parameters in order to create an Outcomes object  
num_lines_bid_on - required parameter, an int of the number of lines the user has bid on   
bid_per_line - required parameter, an int of the number of pennies bid per line  
board_to_compare - required parameter, the board_compared from the Display object  
total_win - set to 0, the final result of the wins from the user  

## Methods

The Outcomes class has 6 methods  
1. create_lines - examines each line the user has bid on. Uses the LINE_COMBOS_CONFIGURATIONS dictionary to check which symbols are at the associated spots per line. From there, each line is stored as a string in the LINES_COMBOS_OUTCOMES dictionary  
2. calculate_earning_per_line - calculates an individual line's total earnings, based on the bid_per_line, the base payout for the symbol, and if either 4 or 5 symbols match on a line, the FOUR_LINE_BONUS or FIVE_LINE_BONUS respectively
3. calculate_total_same - a static method that loops through a line, and returns the number of symbols that match up going left to right. 
4. sum_each_line_winning - loops through all the entries in the LINE_COMBOS_OUTCOMES dictionary. First calls calculate_total_same to check how many items in that line match up. Next, calls calculate_earning_per_line to see how much the user has won on that line. Afterwards, it is added to an accumulator. Once all lines have been looped through, and appropriate messages have been displayed, the total amount won is returned. 
5. display_total_winnings - calls sum_each_line_winning to get the total amount won. Displays an appropriate final messages based on whether or not the user has won anything, and returns the total winnings. 
6. reset_values - resets all the values of the LINES_COMBOS_OUTCOMES dictionary to None, and the total_win to 0  

# main.py

Contains the main method, which acts to organize the User, Display, and Outcomes classes into the appropriate game flow for the user.
The main method contains a while loop, which calls upon the various methods within these 3 classes when appropriate. 

# keyboard_controls.py
Contains 2 methods used for turning off and on the user's keyboard. These were added to fix a bug where a user hitting keys could disrupt the flow of the game.
1. disable_keyboard - loops through every key and shuts off its functionality
2. enable_keyboard - loops through every key and turns on its functionality. 


# Future Prospects
1. Add a GUI
>I would love it if this could eventually become an actual GUI app, which mimics the look and feel of a real slot machine more closely. 
>I previously attempted to use tkinter to display the emojis. However, due to the limitations of tkinter, it is unable to display the emojis in full color
>I understand that there is a way to display an image of the emoji on screen, which will preserve the full color. 
>However, I am simply unwilling to take the time to make this happen at the moment, as there are other project I need to work on. 

