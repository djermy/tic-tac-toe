game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
p1 = "x"
p2 = "o"

# Prints the board layout as a reference to the player.
def print_board_layout():
    print("Board reference:")
    print("[1|2|3]")
    print("[4|5|6]")
    print("[7|8|9]")

def print_game():
    line1 = "[" + str(game_board[0]) + "|" + str(game_board[1]) + "|" + str(game_board[2]) + "]"
    line2 = "[" + str(game_board[3]) + "|" + str(game_board[4]) + "|" + str(game_board[5]) + "]"
    line3 = "[" + str(game_board[6]) + "|" + str(game_board[7]) + "|" + str(game_board[8]) + "]"
    game = "Game Board:" + "\n" + line1 + "\n" + line2 + "\n" + line3
    print(game)

def turn():
    turn_counter = 0
    for i in range(10):
        move = " "
        turn_counter += 1

        # print game over message after 9 turns played.
        if turn_counter >= 10:
            return print("GAME OVER!")
        # show who's turn it is, and ensures the user inputs a valid value.
        if turn_counter % 2 != 0:
            while move == " ":
                try:
                    move = int(input("Player 1's turn, input a tile to take: "))
                except ValueError:
                    print("Input invalid, Please enter a number from the board reference above.")
            game_board[move-1] = p1
        else:
            while move == " ":
                try:
                    move = int(input("Player 2's turn, input a tile to take: "))
                except ValueError:
                    print("Input invalid, Please enter a number from the board reference above.")
            game_board[move-1] = p2
        print_board_layout()
        print_game()

print_board_layout()
print_game()
turn()