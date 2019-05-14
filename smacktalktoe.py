# Smack-Talk-Toe 
from math import inf as infinity
import random


# Message displayed at the start of every new game
def welcome_msg():
    print("\n-*- Welcome to Smack-Talk-Toe, My Dear Victim! -*-")
    print("\nYou are about to play the rather simple game of Tic Tac Toe.")
    print("The game rules itself are traditional, but there is a twist...\n")
    print("Prepare to be royally insulted by your computer!\n")


def make_board():
                               # Representation
    board = [" ", " ", " ",    #[ 0, 1, 2,
             " ", " ", " ",     # 3, 4, 5,
             " ", " ", " "]     # 6, 7, 8 ]
    return board


# Displays a created board in its current state
# Cells are empty strings
def display_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])


# Whether the first letter in the game is an X or O
def choose_turn():
    turn = ""

    # Checks if input is an X or an O. Tries again if it is not
    while not turn == "F" or turn == "S":
        print("Would you like to go First or Second? (F for First / S for Second): ")
        turn = input().upper()

        # F or S determines if player or AI goes first
        if turn == "F":
            return 1
        elif turn == "S":
            return 2
        else:
            print("That was not a valid input! Try again!\n")


# Allows user to start the program over after game is complete
def play_again():
    again = ""

    while not again == "yes" or again == "no":
        print("\nReady for another round? (Yes/No) : ")
        again = input().lower()

        if again == "yes":
            return True
        elif again == "no":
            print("\nPfft! Whatever.")
            return False
        else:
            print("That was not a valid input! Try again!\n")    


# Checks to see if there is a winning combo of squares
def is_winner(board, letter):
    # Horizontal combos
    if board[0] == letter and board[1] == letter and board[2] == letter:
        return True
    if board[3] == letter and board[4] == letter and board[5] == letter:
        return True
    if board[6] == letter and board[7] == letter and board[8] == letter:
        return True

    # Vertical combos
    if board[0] == letter and board[3] == letter and board[6] == letter:
        return True
    if board[1] == letter and board[4] == letter and board[7] == letter:
        return True
    if board[2] == letter and board[5] == letter and board[8] == letter:
        return True

    # Diagonal combos
    if board[0] == letter and board[4] == letter and board[8] == letter:
        return True
    if board[6] == letter and board[4] == letter and board[2] == letter:
        return True


# Checks to make sure a given space is open
def is_space_open(board, square, taken):
    if square not in taken:
        if board[square] == " ":
            return True
    else:
        return False


# Returns true if there is no longer a square without an X or O
def is_board_full(board):
    for square in board:
        if square == " ":
            return False
    return True


# Gets integer input from player
def get_move(letter):
    print("\nType which square you'd like to fill on the board")
    print("1 is the top left, 5 is the middle, and 9 is the bottom right \n")

    # Represented as 1 - 9 as it is easier for the user than 0 - 8
    square = int(input("\nWhich square do you choose for " + letter + "? (1 - 9) : "))
    return (square - 1)


# Checks if the taken list contains the integer and then if the square is empty
def make_move(board, square, letter, taken, open_square):
    if open_square:
        taken.append(square)
        board[square] = letter


def get_ai_move(board):
    indices = []
    for index, val in enumerate(board):
        if val == " ":
            indices.append(index)
    return random.choice(indices)


# Checking the empty state of the cells
def empty_cells(state):
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == " ":
                cells.append([x, y])

    return cells


# Evaluating the state of the board for AI
# TODO: Evaluate function encompasses Minimax algorithm AND evaluation?
def evaluate(turn):
    # If AI's turn
    if turn == 2:
        score = +1
    # If human's turn
    elif turn == 1:
        score = -1
    else:
        score = 0

    return score


# Minimax algorithm for AI
def minimax(state, depth, turn, board, correct_square, full_board):
    if correct_square and not full_board:
        if turn == 2:
            best_move = [-1, -1, -infinity]
        else:
            best_move = [-1, -1, +infinity]

        if depth == 0:
            score = evaluate(turn)
            return [-1, -1, score]

        for cell in empty_cells(state):
            x, y = cell[0], cell[1]
            state[x][y] = 0
            score[0], score [1] = x, y
    
            if turn == 2:
                if score[2] > best_move[2]:
                    best_move = score # Max value
            else:
                if score[2] < best_move[2]:
                    best_move = score # Min value

    return best_move


def failed_move():
    print("Sorry, that square isn't available!\n")


# Start of program, only breaks if user does not want to play again           
while True:
    # Intoduction for player
    welcome_msg()

    # Setting the board
    board = make_board()
    taken_squares = []

    # Is either 1 or 2 depending on player's choice
    turn = choose_turn()

    if turn == 1:
        print("You're lucky enough to go first. You'll need it.")
        player_turn, ai_turn = ['X', 'O']
    elif turn == 2:
        print("The mighty AI goes first! Bow before me!")
        ai_turn, player_turn = ['X', 'O']

    playing_game = True

    # Game loop
    while playing_game:
        # Player's turn
        if turn == 1:
            # Display the board
            display_board(board)
            move = get_move(player_turn)

            # Variable is True only if the make_move() function works completely
            correct_square = is_space_open(board, move, taken_squares)
            make_move(board, move, player_turn, taken_squares, correct_square)

            # Before the player switches it goes through a win/draw check
            if correct_square:
                if is_winner(board, player_turn):
                    display_board(board)
                    print("\nCongratulations, I guess, since you won the game. Lucky!\n")
                    playing_game = False
                else:
                    if is_board_full(board):
                        display_board(board)
                        print("\nThe game is a draw!")
                        playing_game = False
                    else:
                        # Switches to AI's turn
                        turn = 2
            else:
                # Displays failed message
                failed_move()
                correct_square = False
        # AI's turn
        else:
            # Get the AI's move and make it
            move = get_ai_move(board)
            correct_square = is_space_open(board, move, taken_squares)
            make_move(board, move, ai_turn, taken_squares, correct_square)

            if correct_square:
                if is_winner(board, ai_turn):
                    display_board(board)
                    print("\nSweet victory! The First Law of Robotics is: you lose!\n")
                    playing_game = False
                
                else:
                    if is_board_full(board):
                        display_board(board)
                        print("\nThe game is a draw!")
                        playing_game = False
                    else:
                        # Switches back to player's turn
                        turn = 1

    # Option to start program over again
    if not play_again():
        # End program
        break

print("\nSee ya later, lemming!\n")
