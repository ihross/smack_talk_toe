# Smack Talk Toe

"""
--Psuedo code--

Remaining Initial Tasks:
-Two-player functionality
-Replace 2nd player with AI
-AI analysis of position
-Write smack talking statements
-Apply smack talking to analysis

"""

class Board(object):
    # Initializes list of 9 squares
    def __init__(self):
        self.squares = [" "]*9

    # Display the board
    def display(self):
        print(self.squares[0], "|", self.squares[1], "|", self.squares[2])
        print("---------")
        print(self.squares[3], "|", self.squares[4], "|", self.squares[5])
        print("---------")
        print(self.squares[6], "|", self.squares[7], "|", self.squares[8])

    # Reset the board
    def reset(self):
        self.cells = [" "]*9

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


class Player(object):
    # Sets up player class
    def __init__(self, human_or_ai, letter):
        self.human_or_ai = human_or_ai
        self.letter = letter
        self.score = 0

    # Naming this instance of a player
    def set_player_name(self, player_name):
        self.name = player_name

        print("What is your name?")
        player_name = input()
        print("Welcome to the hardest challenge of your life, {}!".format(player_name))

    # Naming the AI
    def set_ai_name(self, ai_name):
        self.name = ai_name

        print("What would you like to call me?")
        ai_name = input()
        print("Fine, you can call me {}. You're gonna lose anyway!".format(ai_name))

# Brief welcome message
def welcome_msg():
    print("-*- Welcome to Smack-Talk-Toe, Dear Player! -*-")


# Info displayed about the AI
def info():
    print("\nYou are about to play the rather simple game of Tic Tac Toe.")
    print("The game rules itself are traditional, but there is a twist...\n")
    print("Prepare to be royally insulted by your computer!\n")


# Choose to play again
def play_again():
    again = ""
    while not again == "yes" or again == "no":
        print("\nReady for another round? (Yes/No) : ")
        again = input().lower()

        if again == "yes":
            return True
        elif again == "no":
            print("\nPfft! Giving up already...\n")
            return False
        else:
            print("That was not a valid input! Try again!\n")  

# Start of program
while True:
    # Temporary global variables for testing
    human = "Human"
    ai = "AI"
    playing_game = True

    # Creates object of Board class
    board = Board()
    human = Player(human, "X")
    comp = Player(ai, "O")

    while playing_game:
        welcome_msg()
        info()

        human.set_player_name(human)
        comp.set_ai_name(ai)

        board.display()

        if not play_again():
            playing_game = False

    break

print("\nThanks for playing anyway, loser!\n")