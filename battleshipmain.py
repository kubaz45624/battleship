import battleship
import os
import time

def battleship_game(game_mode, size, turn_limit = None):
    if game_mode == 1:
        pass
    else:
        player_1_game_board = battleship.set_gameboard(size)
        player_1_board_display = battleship.set_gameboard(size)
        player_2_game_board = battleship.set_gameboard(size)
        player_2_board_display = battleship.set_gameboard(size)

    battleship.place_ships(player_1_game_board, 1, size)
    os.system("cls")
    input("Next player's placement phase. ")
    battleship.place_ships(player_2_game_board, 2, size)
    os.system("cls")

    while turn_limit != 0:
        player_1_coords = battleship.shooting_ships(player_1_board_display, 1)
        battleship.mark_move_on_board(player_2_game_board, player_1_board_display, 1, player_1_coords[0], player_1_coords[1])
        time.sleep(1)
        os.system("cls")
        if battleship.has_won(player_2_game_board, 1) == True:
            print("Player 1 wins!")
            break
        player_2_coords = battleship.shooting_ships(player_2_board_display, 2)
        battleship.mark_move_on_board(player_1_game_board, player_2_board_display, 2, player_2_coords[0], player_2_coords[1])
        time.sleep(1)
        os.system("cls")
        if battleship.has_won(player_1_game_board, 2) == True:
            print("Player 2 wins!")
            break

def main_menu():
    print("Welcome!")
    
    game_options = input("Choose game mode:\n1. Single player\n2. Multiplayer\n")
    while not game_options.isdigit() or (int(game_options) == 2 or int(game_options) == 1):
        
        game_options = input("Choose game mode:\n1. Single player\n2. Multiplayer\n")
    
    board_size = input("Choose board size 5-10: ")
    while not board_size.isdigit():
        if (int(board_size) >= 5 and int(board_size) <= 10):
            break
        board_size = input("Choose board size 5-10: ")
    
    turn_limit = input("Choose turn limit: ")
    while not turn_limit.isdigit():
        if (int(turn_limit) >= 5 and int(turn_limit) <= 50):
            break
        turn_limit = input("Choose turn limit: ")

    print(game_options, board_size, turn_limit)


if __name__ == '__main__':
    main_menu()