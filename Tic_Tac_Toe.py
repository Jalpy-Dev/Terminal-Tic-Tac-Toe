import sys
import os


def display_board(board):

    # Clear Terminal
    os.system("clear")

    # Print Squares Of Board
    for i in range(0, 9, 3):  # Loop through three times (One for each row)
        print(
            "   |   |   ",  # Fancy Dividers
            f"\n {board[6 - i]} | {board[7 - i]} | {board[8 - i]} ",  # Print values in middle of square
            "\n   |   |   ",
        )
        if i < 6:  # Dont print bottom line if its the last row
            print("--- --- ---")

    print("\n")


def player_input():

    choice = ""
    acceptablerange = range(1, 10)  # Set acceptable range to numbers 1-9
    isvalid = False

    while (
        choice.isdigit is False or isvalid is False
    ):  # Repeat until user input is valid

        choice = input("Please input an index value (1 - 9): ")

        if choice == "quit":
            sys.exit()
        elif choice.isdigit():
            if int(choice) in acceptablerange:
                isvalid = True
        else:
            print("\nPlease choose a valid index! \n")

    return int(choice)


def place_marker(board, mark, location):

    # Set location on board to mark
    board[location - 1] = mark

    return board


def win_check(board, mark):

    # Check for win horizontally
    """
    Wind Conditions
    0 = 1 = 2
    3 = 4 = 5
    6 = 7 = 8
    """
    for row in range(0, 9, 3):
        count = 0
        for item in range(0, 3):
            if board[item + row] == mark:
                count += 1
        if count == 3:
            return True

    # Check for win veritcally
    """
    Win Conditions
    0 = 3 = 6
    1 = 4 = 7
    2 = 5 = 8
    """
    for column in range(0, 3):
        count = 0
        for i in range(0, 9, 3):
            if board[column + i] == mark:
                count += 1
        if count == 3:
            return True

    # Check for win diagonally
    """
    Win Conditions
    0 = 4 = 8
    2 = 4 = 6
    """
    if board[0] == mark:
        if board[0] == board[4] and board[4] == board[8]:
            return True
    elif board[2] == mark:
        if board[2] == board[4] and board[4] == board[6]:
            return True

    return False


print("Welcome to Tic Tac Toe!")

gameBoard = list(range(1, 10))

plays = 0

while True and plays < 9:
    display_board(gameBoard)

    # Player 1 Input
    print("Player 1: ")
    p1Input = player_input()

    # Add player 1's move to board
    place_marker(gameBoard, "X", p1Input)
    display_board(gameBoard)

    # Check if player 1 has won
    if win_check(gameBoard, "X"):
        print("Congratulations Player 1, you won!")
        break

    # Player 2 Input
    print("Player 2: ")
    p2Input = player_input()

    # Add player 2's move to board
    place_marker(gameBoard, "O", p2Input)
    display_board(gameBoard)

    # Check if player 2 has won
    if win_check(gameBoard, "O"):
        print("Congratulations Player 2, you won!")
        break

    plays += 2

print("Game ended in a tie :/")
