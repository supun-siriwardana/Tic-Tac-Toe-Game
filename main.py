
# board

initial_board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]


def game_board(value):
    print("\n")
    print("\t\t\t        |        |")
    print("\t\t\t   {}    |   {}    |  {}".format(value[0], value[1], value[2]))
    print("\t\t\t _______|________|_______")
    print("\t\t\t        |        |")
    print("\t\t\t   {}    |   {}    |  {}".format(value[3], value[4], value[5]))
    print("\t\t\t _______|________|_______")
    print("\t\t\t        |        |")
    print("\t\t\t   {}    |   {}    |  {}".format(value[6], value[7], value[8]))
    print("\t\t\t        |        |")
    print("\n")


# play game
def game_play():
    print("Player 1")
    player_1 = input("Enter your Name ")
    print("Player 2")
    player_2 = input("Enter your Name ")
    turn = player_1
    count = 0

    for x in range(10):
        game_board(initial_board)

        print("It's your turn " + turn + ", which place to move ?")
        print("---Choose a number between 1 to 9 ----")

        try:
            move_position = int(input())
        except ValueError:
            print("----Wrong Input!!! ----")
            continue

        move_position = move_position - 1
        if move_position > 8:
            print("--- Wrong input!!! Enter value between 1 to 9")
        else:

            if initial_board[int(move_position)] == " ":
                if turn == player_1:
                    mark = "X"
                else:
                    mark = "O"
                initial_board[int(move_position)] = mark
                count += 1
                if game_win(mark, turn):
                    game_board(initial_board)
                    break

            else:
                print("!!!---This place is already filled---!!!\nChoose another place")
                try:
                    move_position = int(input())
                except ValueError:
                    print("----Wrong Input!!! ----")
                    continue
                move_position = move_position - 1
                if turn == player_1:
                    mark = "X"
                else:
                    mark = "O"
                initial_board[int(move_position)] = mark
                count += 1
                if game_win(mark, turn):
                    game_board(initial_board)
                    break

            if turn == player_1:
                turn = player_2
            else:
                turn = player_1

        if count == 9:
            print("---- !!! GAME OVER !!! ----\n       It's a Tie")
            game_board(initial_board)
            break


def game_win(mark, turn):
    for row_check in range(0, 8, 3):
        if initial_board[row_check] == initial_board[row_check + 1] == initial_board[row_check + 2] == mark:
            print("Congratulations ! " + turn + ", You won the game ")
            print("---- !!! GAME OVER !!! ----")
            return True

    for column_check in range(3):
        if initial_board[column_check] == initial_board[column_check + 3] == initial_board[column_check + 6] == mark:
            print("Congratulations ! " + turn + ", You won the game ")
            print("---- !!! GAME OVER !!! ----")
            return True

    diagonal_check = 4
    if initial_board[diagonal_check - 4] == initial_board[diagonal_check] == initial_board[diagonal_check + 4] \
            == mark or initial_board[diagonal_check - 2] == initial_board[diagonal_check] == initial_board[
        diagonal_check + 2] \
            == mark:
        print("Congratulations ! " + turn + ", You won the game ")
        print("---- !!! GAME OVER !!! ----")
        return True


while True:
    game_play()
    new_game = input("Do you want to play again YES: Y / NO: N ?")
    if new_game == "Y" or new_game == "y":
        exec(open("main.py").read())

    else:
        break
