#2. one fuction to shoot ship
import random
import battleship
import colorama
import time
import os
x_mark = colorama.Fore.GREEN + "X" + colorama.Style.RESET_ALL
h_mark = colorama.Fore.LIGHTRED_EX + "H" + colorama.Style.RESET_ALL
s_mark = colorama.Fore.RED + "S" + colorama.Style.RESET_ALL
o_mark = colorama.Fore.LIGHTBLUE_EX + "0" + colorama.Style.RESET_ALL
m_mark = colorama.Fore.BLUE + "M" + colorama.Style.RESET_ALL


def check_ends(game_board, coors, ship_size, possible_moves, s = 1):
    #gather posible ends of ship and return random coords
    possible_ends = []
    if coors[0] - ship_size+s >= 0 and [coors[0] - ship_size+s, coors[1]] in possible_moves:
        possible_ends.append([coors[0] - ship_size+s, coors[1]])
    if coors[0] + ship_size-s < len(game_board) and [coors[0] + ship_size-s, coors[1]] in possible_moves:
        possible_ends.append([coors[0] + ship_size-s, coors[1]])
    if coors[1] - ship_size+s >= 0 and [coors[0], coors[1] - ship_size+s] in possible_moves:
        possible_ends.append([coors[0], coors[1] - ship_size+s])
    if coors[1] + ship_size-s < len(game_board) and [coors[0], coors[1] + ship_size-s] in possible_moves:
        possible_ends.append([coors[0], coors[1] + ship_size-s])
    
    return possible_ends


def ai_place_ship(game_board, board_size):
    if board_size < 7:
        dict_of_ships = {"CRUISER": 3, "SUBMARINE": 3, "DESTROYER": 2}
    elif board_size < 9:
        dict_of_ships = {"BATTLESHIP": 4, "CRUISER": 3, "SUBMARINE": 3, "DESTROYER": 2}
    else:
        dict_of_ships = {"CARRIER": 5, "BATTLESHIP": 4, "CRUISER": 3, "SUBMARINE": 3, "DESTROYER": 2}
    #gather possible moves
    possible_moves = []
    for i in range(0, len(game_board)):
        for j in range(0, len(game_board[i])):
            if game_board[i][j] == o_mark:
                possible_moves.append([i, j])

    for i in dict_of_ships.keys():
        random_choose = random.choice(possible_moves)
        random_end_chose = random.choice(check_ends(game_board, random_choose, dict_of_ships[i], possible_moves))
        s = battleship.check_board(game_board, f"{chr(random_choose[0]+64)}{random_choose[1]}", f"{chr(random_end_chose[0]+64)}{random_end_chose[1]}", dict_of_ships[i])
        while (battleship.check_ship_untouched(game_board, s, dict_of_ships[i]) == False) or (battleship.check_ship_untouched(game_board, s, dict_of_ships[i]) == -1):
            random_choose = random.choice(possible_moves)
            random_end_chose = random.choice(check_ends(game_board, random_choose, dict_of_ships[i], possible_moves))
            s = battleship.check_board(game_board, f"{chr(random_choose[0]+64)}{random_choose[1]}", f"{chr(random_end_chose[0]+64)}{random_end_chose[1]}", dict_of_ships[i])

        for i in range(0, len(s)):
            game_board[s[i][0]][s[i][1]] = x_mark
            possible_moves.remove(s[i])

def chcec_for_next_hit(game_board_display, row, col, direct, setup):
    temp = []
    while (col > 0 and col < len(game_board_display)) and (row > 0 and row < len(game_board_display)):
        if game_board_display[row][col] == o_mark:
            temp.append([row, col])
            break
        elif game_board_display[row][col] == m_mark:
            break

        if direct == "-" and setup == "row":
            row -= 1
        elif direct == "+" and setup == "row":
            row += 1
        elif direct == "-" and setup == "col":
            col -= 1
        else:
            col += 1
    return temp

def ai_shot_ships(game_board_display, game_board):
    battleship.display_board(game_board_display)
    time.sleep(1)
    possible_moves = []
    hit_shots = []
    for i in range(0, len(game_board_display)):
        for j in range(0, len(game_board_display[i])):
            if game_board_display[i][j] == o_mark:
                possible_moves.append([i, j])
            elif game_board_display[i][j] == h_mark:
                hit_shots.append([i, j])
    #remove field next to sunken ship
    for i in range(0, len(game_board_display)):
        for j in range(0, len(game_board_display[i])):
            if game_board_display[i][j] == s_mark:
                if [i+1, j] in possible_moves:
                    possible_moves.remove([i+1, j])
                if [i-1, j] in possible_moves:
                    possible_moves.remove([i-1, j])
                if [i, j+1] in possible_moves:
                    possible_moves.remove([i, j+1])
                if [i, j-1] in possible_moves:
                    possible_moves.remove([i, j-1])
    
    if len(hit_shots) == 0:
        random_free = random.choice(possible_moves)
        os.system("cls")
        battleship.mark_move_on_board(game_board, game_board_display, "computer", random_free[0], random_free[1])
    elif len(hit_shots) == 1:
        next_hit = check_ends(game_board_display, hit_shots[0], 1, possible_moves, s = 0)
        next_hit_random = random.choice(next_hit)
        os.system("cls")
        battleship.mark_move_on_board(game_board, game_board_display, "computer", next_hit_random[0], next_hit_random[1])
    else:
        if hit_shots[0][0] == hit_shots[1][0]:
            possible_hits = chcec_for_next_hit(game_board_display, hit_shots[0][0], hit_shots[0][1], "+", "col") + chcec_for_next_hit(game_board_display, hit_shots[0][0], hit_shots[0][1], "-", "col")
            possible_hits_random = random.choice(possible_hits)
            os.system("cls")
            battleship.mark_move_on_board(game_board, game_board_display, "computer", possible_hits_random[0], possible_hits_random[1])
        else:
            possible_hits = chcec_for_next_hit(game_board_display, hit_shots[0][0], hit_shots[0][1], "+", "row") + chcec_for_next_hit(game_board_display, hit_shots[0][0], hit_shots[0][1], "-", "row")
            possible_hits_random = random.choice(possible_hits)
            os.system("cls")
            battleship.mark_move_on_board(game_board, game_board_display, "computer", possible_hits_random[0], possible_hits_random[1])



if __name__ == '__main__':
    d = [[' ', '1', '2', '3', '4', '5'], ['A', 'H', '0', 'H', '0', '0'], ['B', '0', '0', '0', '0', '0'], ['C', '0', '0', '0', '0', '0'], ['D', '0', '0', '0', '0', '0'], ['E', '0', '0', '0', '0', '0']]
    """ s = battleship.set_gameboard(10)
    ai_place_ship(s, 10)
    
    #s = colorama.Fore.RED + s + colorama.Style.RESET_ALL
    
    for i in range(0, len(s)):
        print(colorama.Fore.RED + " ".join(s[i]) + colorama.Style.RESET_ALL) """
    g = [[' ', '1', '2', '3', '4', '5'], ['A', 'H', 'X', 'H', '0', '0'], ['B', '0', 'M', '0', '0', '0'], ['C', '0', '0', '0', '0', '0'], ['D', '0', '0', '0', '0', '0'], ['E', '0', '0', '0', '0', '0']]
    """ ai_shot_ships(d, g)
    for i in range(0, len(d)):
        print(colorama.Fore.RED + " ".join(d[i]) + colorama.Style.RESET_ALL) """
    s = colorama.Fore.RED + "asd" + colorama.Style.RESET_ALL

    f = ["ASd", s, "dsa"]
    h =  colorama.Fore.RED + "asd" + colorama.Style.RESET_ALL
    print(s in f)

    