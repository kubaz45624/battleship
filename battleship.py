# 1. functrion init board for players(size)
# 2. place ship on board
# 3. shooting phase displaye player number and board. valid correct input. mark hited field
# 4. game_mode function setup game options(single/multi, board size, ship sizes and number)
# 5. AI can play
# 6. 5 ships lengte 5, 4, 3, 3, 2
import zipapp
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
    cor1 = list(cor1)
    cor2 = list(cor2)
    cor1[0] = ord(cor1[0]) - 64
    cor1[1] = int(cor1[1])
    cor2[0] = ord(cor2[0]) - 64
    cor2[1] = int(cor2[1])
    right_coor = []

    if cor1[0] == cor2[0]:
        if (cor1[1] + ship_size - 1 == cor2[1]) or (cor2[1] + ship_size - 1 == cor1[1]):
            if ("".join(game_board[cor1[0]][cor1[1]: (cor2[1]+1)]) == "0" * ship_size) or ("".join(game_board[cor1[0]][cor2[1]: (cor1[1]+1)]) == "0" * ship_size):
                for i in range(min(cor1[1], cor2[1]), max(cor1[1], cor2[1])+1):
                    right_coor.append([cor1[0], i])
    elif cor1[1] == cor2[1]:
        if (cor1[0] + ship_size - 1 == cor2[0]) or (cor2[0] + ship_size - 1 == cor1[0]):
            if ("".join([el[cor1[1]] for el in game_board[cor1[0]:(cor2[0]+1)]]) == "0" * ship_size) or ("".join([el[cor1[1]] for el in game_board[cor2[0]:(cor1[0]+1)]]) == "0" * ship_size):
                for i in range(min(cor1[0], cor2[0]), max(cor1[0], cor2[0])+1):
                    right_coor.append([i, cor1[1]])
    print(right_coor)
    return right_coor
def place_ships(game_board, player):
    # names, numbers and size of ship
    """ carrier = [1, 5]
    battleship = [1, 4]
    cruiser = [1, 3]
    submarine = [1, 3]
    destroyer = [1, 2] """
    #dict_of_ships = {"carrier": 5, "battleship": 4, "cruiser": 3, "submarine": 3, "destroyer": 2}
    display_board(game_board)
    

    #coordinates_ships = input(f"Place your ships on board {str(dict_of_ships)} (example: carrier A1 A5): ")
    #while len(dict_of_ships) != 0:

    


s = set_gameboard(7)
display_board(s)
#place_ships(s, 1)
print(check_board(s, "G4", "C5", 5))


