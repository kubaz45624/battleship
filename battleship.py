# 1. functrion init board for players(size)+
# 2. place ship on board
# 3. shooting phase displaye player number and board. valid correct input. mark hited field
# 4. game_mode function setup game options(single/multi, board size, ship sizes and number)
# 5. AI can play
# 6. 5 ships lengte 5, 4, 3, 3, 2 +
# 7. difrent numbers of ship in difrent size of board+
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
                    game_board[i].append("0")
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
            if ("".join(game_board[cor1[0]][cor1[1]: (cor2[1]+1)]) == "0" * ship_size) or ("".join(game_board[cor1[0]][cor2[1]: (cor1[1]+1)]) == "0" * ship_size):
                for i in range(min(cor1[1], cor2[1]), max(cor1[1], cor2[1])+1):
                    right_coor.append([cor1[0], i])
    #check vertical
    elif cor1[1] == cor2[1]:
        if (cor1[0] + ship_size - 1 == cor2[0]) or (cor2[0] + ship_size - 1 == cor1[0]):
            if ("".join([el[cor1[1]] for el in game_board[cor1[0]:(cor2[0]+1)]]) == "0" * ship_size) or ("".join([el[cor1[1]] for el in game_board[cor2[0]:(cor1[0]+1)]]) == "0" * ship_size):
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
            if "".join(game_board[right_coor[0][0]+1][right_coor[0][1]:right_coor[len(right_coor)-1][1]+1]) != "0" * ship_size:
                return False
        elif right_coor[0][0] == len(game_board) - 1:
            if "".join(game_board[right_coor[0][0]-1][right_coor[0][1]:right_coor[len(right_coor)-1][1]+1]) != "0" * ship_size:
                return False
        else:
            if "".join(game_board[right_coor[0][0]-1][right_coor[0][1]:right_coor[len(right_coor)-1][1]+1]) != "0" * ship_size or "".join(game_board[right_coor[0][0]+1][right_coor[0][1]:right_coor[len(right_coor)-1][1]+1]) != "0" * ship_size:
                return False

        if right_coor[0][1] != 1 and game_board[right_coor[0][0]][right_coor[0][1]-1] == "X":
            return False

        if (right_coor[len(right_coor)-1][1] != len(game_board) - 1) and game_board[right_coor[0][0]][right_coor[len(right_coor)-1][1]+1] == "X":
            return False
    #check vertical
    else:
        if right_coor[0][1] == 1:
            if "".join([el[right_coor[0][1]+1] for el in game_board[right_coor[0][0]:(right_coor[len(right_coor)-1][0]+1)]]) != "0" * ship_size:
                return False
        elif right_coor[0][1] == len(game_board) - 1:
            if "".join([el[right_coor[0][1]-1] for el in game_board[right_coor[0][0]:(right_coor[len(right_coor)-1][0]+1)]]) != "0" * ship_size:
                return False
        else:
            if "".join([el[right_coor[0][1]-1] for el in game_board[right_coor[0][0]:(right_coor[len(right_coor)-1][0]+1)]]) != "0" * ship_size or "".join([el[right_coor[0][1]+1] for el in game_board[right_coor[0][0]:(right_coor[len(right_coor)-1][0]+1)]]) != "0" * ship_size:
                return False
        
        if right_coor[0][0] != 1 and game_board[right_coor[0][0]-1][right_coor[0][1]] == "X":
            return False
        
        if right_coor[len(right_coor)-1][0] != len(game_board) - 1 and game_board[right_coor[len(right_coor)-1][0]+1][right_coor[0][1]] == "X":
            return False
    return True

def place_ships(game_board, player, board_size):
    # names, numbers and size of ship
    if board_size == 5:
        dict_of_ships = {"CRUISER": 3, "SUBMARINE": 3, "DESTROYER": 2}
    elif board_size == 6:
        dict_of_ships = {"BATTLESHIP": 4, "CRUISER": 3, "SUBMARINE": 3, "DESTROYER": 2}
    else:
        dict_of_ships = {"CARRIER": 5, "BATTLESHIP": 4, "CRUISER": 3, "SUBMARINE": 3, "DESTROYER": 2}

    while len(dict_of_ships) != 0:
        display_board(game_board)
        coordinates_ships = input(f"Place your ships on board {str(dict_of_ships)} (example: CARRIER A1 A5): ").upper()
        coor_list = coordinates_ships.split(" ")

        while (coor_list[0] not in dict_of_ships.keys()) or len(coor_list) != 3:
            print("Invalid input!")
            coordinates_ships = input(f"Place your ships on board {str(dict_of_ships)} (example: CARRIER A1 A5): ").upper()
            coor_list = coordinates_ships.split(" ")
        
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
                    game_board[coor_to_check[i][0]][coor_to_check[i][1]] = "X"
                dict_of_ships.pop(coor_list[0])
    


s = set_gameboard(5)
""" print(s)
d = [[' ', '1', '2', '3', '4', '5'], ['A', '0', '0', '0', '0', '0'], ['B', '0', '0', '0', '0', '0'], ['C', '0', '0', '0', '0', '0'], ['D', '0', '0', '0', '0', '0'], ['E', '0', 'X', '0', '0', '0']]
ss = check_board(d, "B2", "D2", 3)
display_board(s)
print(ss)
print(check_ship_untouched(d, ss, 3)) """
place_ships(s, 1, 5)
print(s)
