import os
import time
import sys
import colorama

x_mark = colorama.Fore.GREEN + "X" + colorama.Style.RESET_ALL
h_mark = colorama.Fore.LIGHTRED_EX + "H" + colorama.Style.RESET_ALL
s_mark = colorama.Fore.RED + "S" + colorama.Style.RESET_ALL
o_mark = colorama.Fore.LIGHTBLUE_EX + "0" + colorama.Style.RESET_ALL
m_mark = colorama.Fore.BLUE + "M" + colorama.Style.RESET_ALL

def set_gameboard(board_size):
    #init board of various size
    game_board = []
    for i in range(board_size+1):
        game_board.append([])
        for j in range(board_size+1):
            if i == 0:
                if j != 0:
                    game_board[i].append(str(j))
                else:
                    game_board[i].append(" ")
            else:
                if j != 0:
                    game_board[i].append(o_mark)
                else:
                    game_board[i].append(chr(i + 64))
    return game_board

def display_board(game_board):
    for i in range(len(game_board)):
        print(" ".join(game_board[i]))

def check_board(game_board, cor1, cor2, ship_size):
    #check for empty field in player coordinates
    cor1 = list(cor1)
    cor2 = list(cor2)
    cor1[0] = ord(cor1[0]) - 64
    cor1[1] = int(cor1[1])
    cor2[0] = ord(cor2[0]) - 64
    cor2[1] = int(cor2[1])
    right_coor = []
    #check horizontally
    if cor1[0] == cor2[0]:
        if (cor1[1] + ship_size - 1 == cor2[1]) or (cor2[1] + ship_size - 1 == cor1[1]):
            if ("".join(game_board[cor1[0]][cor1[1]: (cor2[1]+1)]) == o_mark * ship_size) or ("".join(game_board[cor1[0]][cor2[1]: (cor1[1]+1)]) == o_mark * ship_size):
                for i in range(min(cor1[1], cor2[1]), max(cor1[1], cor2[1])+1):
                    right_coor.append([cor1[0], i])
    #check vertical
    elif cor1[1] == cor2[1]:
        if (cor1[0] + ship_size - 1 == cor2[0]) or (cor2[0] + ship_size - 1 == cor1[0]):
            if ("".join([el[cor1[1]] for el in game_board[cor1[0]:(cor2[0]+1)]]) == o_mark * ship_size) or ("".join([el[cor1[1]] for el in game_board[cor2[0]:(cor1[0]+1)]]) == o_mark * ship_size):
                for i in range(min(cor1[0], cor2[0]), max(cor1[0], cor2[0])+1):
                    right_coor.append([i, cor1[1]])

    return right_coor

def check_ship_untouched(game_board, right_coor, ship_size):
    #return True if no ship in range
    if len(right_coor) == 0:
        return -1
    
    #check horizontally
    elif right_coor[0][0] == right_coor[len(right_coor)-1][0]:
        if right_coor[0][0] == 1:
            if "".join(game_board[right_coor[0][0]+1][right_coor[0][1]:right_coor[len(right_coor)-1][1]+1]) != o_mark * ship_size:
                return False
        elif right_coor[0][0] == len(game_board) - 1:
            if "".join(game_board[right_coor[0][0]-1][right_coor[0][1]:right_coor[len(right_coor)-1][1]+1]) != o_mark * ship_size:
                return False
        else:
            if "".join(game_board[right_coor[0][0]-1][right_coor[0][1]:right_coor[len(right_coor)-1][1]+1]) != o_mark * ship_size or "".join(game_board[right_coor[0][0]+1][right_coor[0][1]:right_coor[len(right_coor)-1][1]+1]) != o_mark * ship_size:
                return False

        if right_coor[0][1] != 1 and game_board[right_coor[0][0]][right_coor[0][1]-1] == x_mark:
            return False

        if (right_coor[len(right_coor)-1][1] != len(game_board) - 1) and game_board[right_coor[0][0]][right_coor[len(right_coor)-1][1]+1] == x_mark:
            return False
    #check vertical
    else:
        if right_coor[0][1] == 1:
            if "".join([el[right_coor[0][1]+1] for el in game_board[right_coor[0][0]:(right_coor[len(right_coor)-1][0]+1)]]) != o_mark * ship_size:
                return False
        elif right_coor[0][1] == len(game_board) - 1:
            if "".join([el[right_coor[0][1]-1] for el in game_board[right_coor[0][0]:(right_coor[len(right_coor)-1][0]+1)]]) != o_mark * ship_size:
                return False
        else:
            if "".join([el[right_coor[0][1]-1] for el in game_board[right_coor[0][0]:(right_coor[len(right_coor)-1][0]+1)]]) != o_mark * ship_size or "".join([el[right_coor[0][1]+1] for el in game_board[right_coor[0][0]:(right_coor[len(right_coor)-1][0]+1)]]) != o_mark * ship_size:
                return False
        
        if right_coor[0][0] != 1 and game_board[right_coor[0][0]-1][right_coor[0][1]] == x_mark:
            return False
        
        if right_coor[len(right_coor)-1][0] != len(game_board) - 1 and game_board[right_coor[len(right_coor)-1][0]+1][right_coor[0][1]] == x_mark:
            return False
    return True

def place_ships(game_board, player, board_size):
    # names, numbers and size of ship
    if board_size < 7:
        dict_of_ships = {"CRUISER": 3, "SUBMARINE": 3, "DESTROYER": 2}
    elif board_size < 9:
        dict_of_ships = {"BATTLESHIP": 4, "CRUISER": 3, "SUBMARINE": 3, "DESTROYER": 2}
    else:
        dict_of_ships = {"CARRIER": 5, "BATTLESHIP": 4, "CRUISER": 3, "SUBMARINE": 3, "DESTROYER": 2}

    #keep asking till ship in dict_of_ships
    while len(dict_of_ships) != 0:
        time.sleep(1)
        os.system("cls")
        print(f"Player {player}")
        display_board(game_board)
        coordinates_ships = input(f"Place your ships on board {str(dict_of_ships)} (example: CARRIER A1 A5): ").upper()
        coor_list = coordinates_ships.split(" ")

        #keep asking if incorrect ship name or wrong entered
        while (coor_list[0] not in dict_of_ships.keys()) or len(coor_list) != 3:
            print("Invalid input!")
            time.sleep(1)
            os.system("cls")
            print(f"Player {player}")
            display_board(game_board)
            coordinates_ships = input(f"Place your ships on board {str(dict_of_ships)} (example: CARRIER A1 A5): ").upper()
            if coordinates_ships == "QUIT":
                sys.exit()
            coor_list = coordinates_ships.split(" ")
        #check for size
        if not coor_list[1][1] in game_board[0][1:] or not coor_list[2][1] in game_board[0][1:]:
            print("Invalid input!")
        elif not coor_list[1][0] in [el[0] for el in game_board[1:]] or not coor_list[2][0] in [el[0] for el in game_board[1:]]:
            print("Invalid input!")
        else:
            coor_to_check = check_board(game_board, coor_list[1], coor_list[2], dict_of_ships[coor_list[0]])
            if check_ship_untouched(game_board, coor_to_check, dict_of_ships[coor_list[0]]) == False:
                print("Ships are too close!")
            elif check_ship_untouched(game_board, coor_to_check, dict_of_ships[coor_list[0]]) == -1:
                print("Ship is to long/short!")
            else:
                for i in range(0, len(coor_to_check)):
                    game_board[coor_to_check[i][0]][coor_to_check[i][1]] = x_mark
                dict_of_ships.pop(coor_list[0])

def shooting_ships(game_board_display, player):
    possible_moves = []
    for i in range(0, len(game_board_display)):
        for j in range(0, len(game_board_display[i])):
            if game_board_display[i][j] == o_mark:
                possible_moves.append(f"{chr(i + 64)}{j}")
    print(f"Player {player}")
    display_board(game_board_display)
    
    ask_move = input("Choose empty field on board: ").upper()

    while ask_move not in possible_moves:
        print("Invalid input!")
        time.sleep(1)
        os.system("cls")
        print(f"Player {player}")
        display_board(game_board_display)
        ask_move = input("Choose empty field on board: ").upper()
        if ask_move == "QUIT":
            sys.exit()
    
    return ord(ask_move[0]) - 64, int(ask_move[1])

def check_sunk_ship(game_board_display, row, col, direct, setpup):
    #check the coords of sunk ship
    temp = []
    while (col > 0 and col < len(game_board_display)) and (row > 0 and row < len(game_board_display)):
        if game_board_display[row][col] == o_mark:
            break
        elif game_board_display[row][col] == x_mark or game_board_display[row][col] == h_mark:
            temp.append([row, col])

        if direct == "-" and setpup == "row":
            row -= 1
        elif direct == "+" and setpup == "row":
            row += 1
        elif direct == "-" and setpup == "col":
            col -= 1
        else:
            col += 1
    
    return list(temp)

def mark_move_on_board(game_board, game_board_display, player, row, col):
    #mark move on game board
    time.sleep(1)
    os.system("cls")
    if game_board[row][col] == x_mark:
        game_board_display[row][col] = h_mark
        game_board[row][col] = h_mark
        coords_of_sunk = check_sunk_ship(game_board, row, col, "-", "row") + check_sunk_ship(game_board, row, col, "+", "row") + check_sunk_ship(game_board, row, col, "-", "col") +check_sunk_ship(game_board, row, col, "+", "col")
        coords_of_sunk = set(tuple(i) for i in coords_of_sunk)
        coords_of_sunk = list(coords_of_sunk)
        cors_2 = check_sunk_ship(game_board_display, row, col, "-", "row") + check_sunk_ship(game_board_display, row, col, "+", "row") + check_sunk_ship(game_board_display, row, col, "-", "col") +check_sunk_ship(game_board_display, row, col, "+", "col")
        cors_2 = set(tuple(i) for i in cors_2)
        cors_2 = list(cors_2)
        if len(coords_of_sunk) != len(cors_2):
            print(f"Player {player}")
            display_board(game_board_display)
            print("You've hit a ship!")
        else:
            game_board[row][col] = h_mark
            for i in range(0, len(coords_of_sunk)):
                game_board_display[coords_of_sunk[i][0]][coords_of_sunk[i][1]] = s_mark
            print(f"Player {player}")
            display_board(game_board_display)
            print("You've sunk a ship!")     
    else:
        game_board_display[row][col] = m_mark
        print(f"Player {player}")
        display_board(game_board_display)
        print("You've missed!")
    
def has_won(game_board, player):
    for i in range(0, len(game_board)):
        if x_mark in game_board[i]:
            return False
    return True


if __name__ == '__main__':
    s = set_gameboard(5)
    
    d = [[' ', '1', '2', '3', '4', '5'], ['A', 'H', '0', 'H', '0', '0'], ['B', '0', '0', '0', '0', '0'], ['C', 'X', '0', '0', '0', '0'], ['D', '0', '0', '0', 'H', 'X'], ['E', 'X', '0', '0', '0', '0']]
    g = [[' ', '1', '2', '3', '4', '5'], ['A', 'H', 'X', 'H', '0', '0'], ['B', '0', '0', '0', '0', '0'], ['C', 'H', '0', '0', '0', '0'], ['D', '0', '0', '0', 'H', 'X'], ['E', 'X', '0', '0', '0', '0']]
    #print(shooting_ships(s, 1))

    
    s = set_gameboard(5)
    place_ships(s, 1, 5)
    display_board(s)


