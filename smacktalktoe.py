# Smack Talk Toe

"""
--Psuedo code--

Initial Tasks:
-Present information
-Set up board
-Display board
-Two-player functionality
-Win/lose logic
-Allow game to be played again
"""

class Board(object):
    # Initializes list of 9 cells
    def __init__(self):
        self.cells = [" "] * 9

    # Display the board
    def display(self):
        print(self.cells[0], "|", self.cells[1], "|", self.cells[2])
        print("---------")
        print(self.cells[3], "|", self.cells[4], "|", self.cells[5])
        print("---------")
        print(self.cells[6], "|", self.cells[7], "|", self.cells[8])

    # Update the baord
    # def update(self, cell, player):

def welcome_msg():
    print("Hello, Smack Talk Toe, user!")

while True:
    welcome_msg()
    break