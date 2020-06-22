# 1. functrion init board for players(size)
# 2. place ship on board
# 3. shooting phase displaye player number and board. valid correct input. mark hited field
# 4. game_mode function setup game options(single/multi, board size, ship sizes and number)
# 5. AI can play

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


s = set_gameboard(7)

for i in range(len(s)):
    print(s[i])