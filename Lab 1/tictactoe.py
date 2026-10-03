board = [" "] * 9

def display():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def win(p):
    combinations = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in combinations:
        if board[a] == board[b] == board[c] == p:
            return True
    return False

def computer_move():

    # Computer tries to win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if win("O"):
                return
            board[i] = " "

    # Computer blocks human
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if win("X"):
                board[i] = "O"
                return
            board[i] = " "

    # Otherwise choose first empty position
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            return


print("TIC-TAC-TOE")
print("You = X")
print("Computer = O")

for turn in range(9):

    display()

    # Human move
    pos = int(input("Enter position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid position! Try again.")
        continue

    board[pos] = "X"

    if win("X"):
        display()
        print("You Win!")
        break

    if " " not in board:
        display()
        print("Draw!")
        break

    # Computer move
    computer_move()

    print("Computer made a move.")

    if win("O"):
        display()
        print("Computer Wins!")
        break

else:
    display()
    print("Draw!")
