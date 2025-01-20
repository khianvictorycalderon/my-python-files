board = ["——", "——", "——", "——", "——", "——", "——", "——", "——"]  # 9 tiles
X = "❌"
O = "⭕"
charSign = X  # X starts the game

def staticPrint():
    # Display the tile numbers to show user how to pick
    print()
    print("Here are the corresponding numbers for each tile: ")
    print("1 2 3")
    print("4 5 6")
    print("7 8 9")
    print("-----------------------------")
    print()

def printBoard():
    # Print the board representation
    print(f"{board[0]} {board[1]} {board[2]}")
    print(f"{board[3]} {board[4]} {board[5]}")
    print(f"{board[6]} {board[7]} {board[8]}")

def checkWin(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != "——":
            return board[i]
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != "——":
            return board[i]
    
    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != "——":
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != "——":
        return board[2]
    
    # Check for draw (all cells filled and no winner)
    if all(spot != "——" for spot in board):
        return "draw"  # Game is a draw

    # Game is still ongoing
    return None

def playAgain():
    # Ask to play again and reset the game if "yes"
    ui = input("Do you want to play again? 'yes/no'\n--> ").lower()
    if ui == "no":
        print()
        print("Thank you for playing the game!")
        return False  # This will break the loop
    else:
        global board, charSign  # Reset the game
        board = ["——", "——", "——", "——", "——", "——", "——", "——", "——"]
        print()
        printBoard()
        print()
        charSign = X  # X starts the game again
        return True

# Print instructions
staticPrint()

while True:
    printBoard()
    print()

    game_result = checkWin(board)
    if game_result == X:
        print(f"Player {X} won!")
        print()
        if not playAgain():
            break
    elif game_result == O:
        print(f"Player {O} won!")
        print()
        if not playAgain():
            break
    elif game_result == "draw":
        print("It's a draw!")
        print()
        if not playAgain():
            break

    # User input to select spot
    try:
        ui = int(input(f"Player {charSign}, select a spot (1-9): ")) - 1  # Adjust index from 1-9 to 0-8
        print()

        if 0 <= ui < 9 and board[ui] == "——":  # Check if the selected spot is valid
            board[ui] = charSign
            charSign = O if charSign == X else X  # Toggle the character after each move
        else:
            print("Invalid or taken spot, try again!\n")

    except ValueError:
        print("Invalid input, please enter a number between 1 and 9!\n")
