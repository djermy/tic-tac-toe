board_layout = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
p1 = "x"
p2 = "o"

# Prints the board layout as a reference to the player.
def print_board_layout():
    start = 0
    end = 9
    step = 3
    print("Board reference:")
    for i in range(start, end, step):
        x = i
        print(board_layout[x:x+step])

print_board_layout()

def print_game():
    start = 0
    end = 9
    step = 3
    print("Game Board:")
    for i in range(start, end, step):
        x = i
        print(game_board[x:x+step])

print_game()

def turn():
    turn_counter = 0
    for i in range(10):
        move = 0
        turn_counter += 1
        if turn_counter >= 10:
            return print("GAME OVER!")
        if turn_counter % 2 != 0:
            print("Player 1's turn:")
        else:
            print("Player 2's turn:")
        if turn_counter % 2 == 0:
            move = int(input("Input a tile to take: "))
            game_board[move-1] = p1
        else:
            move = int(input("Input a tile to take: "))
            game_board[move-1] = p2
        print_game()
turn()