import battleship
import battleshipai
import os
import time
import colorama

def battleship_game(game_mode, size, turn_limit):
    
    player_1_game_board = battleship.set_gameboard(size)
    player_1_board_display = battleship.set_gameboard(size)
    player_2_game_board = battleship.set_gameboard(size)
    player_2_board_display = battleship.set_gameboard(size)

    battleship.place_ships(player_1_game_board, 1, size)
    os.system("cls")
    if game_mode == 1:
        input("Next player's placement phase. ")
        battleship.place_ships(player_2_game_board, 2, size)
    else:
        battleshipai.ai_place_ship(player_2_game_board, size)
    os.system("cls")

    while turn_limit > 0:
        player_1_coords = battleship.shooting_ships(player_1_board_display, 1)
        battleship.mark_move_on_board(player_2_game_board, player_1_board_display, 1, player_1_coords[0], player_1_coords[1])
        time.sleep(1)
        os.system("cls")
        if battleship.has_won(player_2_game_board, 1) == True:
            print("Player 1 wins!")
            break
        turn_limit -= 1
        if turn_limit < 1:
            break
        if game_mode == 1:
            player_2_coords = battleship.shooting_ships(player_2_board_display, 2)
            battleship.mark_move_on_board(player_1_game_board, player_2_board_display, 2, player_2_coords[0], player_2_coords[1])
        else:
            battleshipai.ai_shot_ships(player_2_board_display, player_1_game_board)
        time.sleep(2)
        os.system("cls")
        if battleship.has_won(player_1_game_board, 2) == True:
            if game_mode == 1:
                print("Player 2 wins!")
            else:
                print("Computer wins!")
            break
        turn_limit -= 1
    
    if turn_limit <= 0:
        print("No more turns, it's a draw!")

def main_menu():
    print("Welcome!")
    
    game_options = input("Choose game mode:\n1. Single player\n2. Multiplayer\n")
    while not game_options.isdigit() or not ((int(game_options) == 2 or int(game_options) == 1)):
        os.system("cls")
        game_options = input("Choose game mode:\n1. Single player\n2. Multiplayer\n")
    os.system("cls")
    
    board_size = input("Choose board size 5-10: ")
    while not board_size.isdigit() or not (int(board_size) >= 5 and int(board_size) <= 10):
        os.system("cls")
        board_size = input("Invalid input! (must be between 5-10) ")
    os.system("cls")
    
    turn_limit = input("Choose turn limit(5-50) or enter \"no limit\": ")
    while not turn_limit.isdigit() or not (int(turn_limit) >= 5 and int(turn_limit) <= 50):
        if turn_limit.lower() == "no limit":
            turn_limit = 204
            break
        os.system("cls")
        turn_limit = input("Invalid input! (must be between 5-50) ")
    os.system("cls")
    
    battleship_game(int(game_options), int(board_size), int(turn_limit))


if __name__ == '__main__':
    main_menu()