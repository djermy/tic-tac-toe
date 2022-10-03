import os
game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
p1 = "x"
p2 = "o"


# Prints the board layout as a reference to the player.
def print_board_layout():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Board reference:")
    print("[1|2|3]")
    print("[4|5|6]")
    print("[7|8|9]")

# Prints the active game board with current moves taken.
def print_game():
    line1 = "[" + str(game_board[0]) + "|" + str(game_board[1]) + "|" + str(game_board[2]) + "]"
    line2 = "[" + str(game_board[3]) + "|" + str(game_board[4]) + "|" + str(game_board[5]) + "]"
    line3 = "[" + str(game_board[6]) + "|" + str(game_board[7]) + "|" + str(game_board[8]) + "]"
    game = "Game Board:" + "\n" + line1 + "\n" + line2 + "\n" + line3
    print(game)

def win_condition_lines():
    # Horizontal lines from top to bottom.
    line_1_h = [game_board[0], game_board[1], game_board[2]]
    line_2_h = [game_board[3], game_board[4], game_board[5]]
    line_3_h = [game_board[6], game_board[7], game_board[8]]

    # Vertical lines from left to right.
    line_1_v = [game_board[0], game_board[3], game_board[6]]
    line_2_v = [game_board[1], game_board[4], game_board[7]]
    line_3_v = [game_board[2], game_board[5], game_board[8]]

    # The two possible diagonals.
    line_1_d = [game_board[0], game_board[4], game_board[8]]
    line_2_d = [game_board[2], game_board[4], game_board[6]]

    all_lines = [line_1_h, line_2_h, line_3_h, line_1_v, line_2_v, line_3_v, line_1_d, line_2_d]
    return all_lines

# Checks if any line is a 3 in a row.
def check_if_game_won(lines):
    for line in lines:
        o_count = 0
        x_count = 0
        for element in line:
            if element == "x":
                x_count += 1
            elif element == "o":
                o_count += 1
            if x_count == 3:
                return True
            elif o_count == 3:
                return True


# show who's turn it is, and ensures the user inputs a valid value.
def valid_move(move, turn_counter):
    turn = ""
    if turn_counter % 2 != 0:
        turn = "Player 1"
    else:
        turn = "Player 2"
    while move == " ":
        try:
            move = int(input(turn + "'s turn, input a tile to take: "))
        except ValueError:
            print("Input invalid, please enter a number from the board reference above.")
            continue
        if move < 1 or move > 9:
            move = " "
            print("Error, please input a number between 1 and 9 (inclusive)")
            continue
        if game_board[move-1] != " ":
            move = " "
            print("This tile is already taken! Please choose another")
            continue
    if turn_counter % 2 != 0:
        game_board[move-1] = p1
    else:   
        game_board[move-1] = p2

def turn():
    turn_counter = 0
    for i in range(10):
        move = " "
        turn_counter += 1
        game_won = check_if_game_won(win_condition_lines())
        # print game over message after 9 turns played.
        if turn_counter >= 10:
            return print("GAME OVER! IT'S A TIE!")
        # ends the game if either wins
        if game_won == True and turn_counter % 2 == 0:
            print("GAME OVER! PLAYER 1 WINS!!!")
            return
        elif game_won == True and turn_counter % 2 != 0:
            print("GAME OVER! PLAYER 2 WINS!!!")
            return
        valid_move(move, turn_counter)
        print_board_layout()
        print_game()
    

print_board_layout()
print_game()
turn()