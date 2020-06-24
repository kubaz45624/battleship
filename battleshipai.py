#2. one fuction to shoot ship
import random
import battleship
import colorama


def check_ends(game_board, coors, ship_size, possible_moves):
    #gather posible ends of ship and return random coords
    possible_ends = []
    if coors[0] - ship_size+1 >= 0 and [coors[0] - ship_size+1, coors[1]] in possible_moves:
        possible_ends.append([coors[0] - ship_size+1, coors[1]])
    if coors[0] + ship_size-1 < len(game_board) and [coors[0] + ship_size-1, coors[1]] in possible_moves:
        possible_ends.append([coors[0] + ship_size-1, coors[1]])
    if coors[1] - ship_size+1 >= 0 and [coors[0], coors[1] - ship_size+1] in possible_moves:
        possible_ends.append([coors[0], coors[1] - ship_size+1])
    if coors[1] + ship_size-1 < len(game_board) and [coors[0], coors[1] + ship_size-1] in possible_moves:
        possible_ends.append([coors[0], coors[1] + ship_size-1])
    
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
            if game_board[i][j] == "0":
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
            game_board[s[i][0]][s[i][1]] = "X"
            possible_moves.remove(s[i])
        
        
if __name__ == '__main__':
    d = [[' ', '1', '2', '3', '4', '5'], ['A', '0', '0', '0', '0', '0'], ['B', '0', '0', '0', '0', '0'], ['C', '0', '0', '0', '0', '0'], ['D', '0', '0', '0', '0', '0'], ['E', '0', '0', '0', '0', '0']]
    s = battleship.set_gameboard(10)
    ai_place_ship(s, 10)
    
    #s = colorama.Fore.RED + s + colorama.Style.RESET_ALL
    
    for i in range(0, len(s)):
        print(colorama.Fore.RED + " ".join(s[i]) + colorama.Style.RESET_ALL)
    
