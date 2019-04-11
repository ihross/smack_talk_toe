# Smack Talk Toe

"""
--Psuedo code--

Remaining Initial Tasks:
-Two-player functionality
-Draw logic
-Allow game to be played again
"""

class Board(object):
    # Initializes list of 9 squares
    def __init__(self):
        self.squares = [" "] * 9

    # Display the board
    def display(self):
        print(self.squares[0], "|", self.squares[1], "|", self.squares[2])
        print("---------")
        print(self.squares[3], "|", self.squares[4], "|", self.squares[5])
        print("---------")
        print(self.squares[6], "|", self.squares[7], "|", self.squares[8])

    # Reset the board
    def reset(self):
        self.cells = [" "] * 9

    # Check for winner
    def winner_check(self, letter):
        # Horizontal combos
        if self.squares[0] == letter and self.squares[1] == letter and self.squares[2] == letter:
            return True
        if self.squares[3] == letter and self.squares[4] == letter and self.squares[5] == letter:
            return True
        if self.squares[6] == letter and self.squares[7] == letter and self.squares[8] == letter:
            return True

        # Vertical combos
        if self.squares[0] == letter and self.squares[3] == letter and self.squares[6] == letter:
            return True
        if self.squares[1] == letter and self.squares[4] == letter and self.squares[7] == letter:
            return True
        if self.squares[2] == letter and self.squares[5] == letter and self.squares[8] == letter:
            return True

        # Diagonal combos
        if self.squares[0] == letter and self.squares[4] == letter and self.squares[8] == letter:
            return True
        if self.squares[6] == letter and self.squares[4] == letter and self.squares[2] == letter:
            return True

    # Check for draw
    def draw_check(self):
        taken = 0
        for square in self.squares:
            if square != " ":
                taken += 1
        if taken == 9:
            return True
        else:
            return False

# Brief welcome message
def welcome_msg():
    print("-*- Welcome to Smack-Talk-Toe, Dear Player! -*-")


# Info displayed about the AI
def info():
    print("\nYou are about to play the rather simple game of Tic Tac Toe.")
    print("The game rules itself are traditional, but there is a twist...\n")
    print("Prepare to be royally insulted by your computer!\n")


# Creates object of Board class
board = Board()

while True:
    welcome_msg()
    info()
    board.display()
    break