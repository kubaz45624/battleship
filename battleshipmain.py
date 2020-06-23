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
    


if __name__ == '__main__':
    battleship_game(2, 5)