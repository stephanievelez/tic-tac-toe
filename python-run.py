import numpy as np
import random 

def sayHello(name):
    print(name)

def create_board():
    board=np.zeros((3,3))
    return board
create_board()

def place(board, player, position):
    if board[position] == 0:
        board[position] = player
    return board

board = create_board()
place(board, 1, (0, 0))

def possibilities(board):
    return list(zip(*np.where(board == 0))) #zip joins a tuple which is the position on the board that has 0
    

possibilities(board)


random.seed(1)

def random_place(board, player):
    selections = possibilities(board)
    if len(selections) > 0: #length is used here to verify that there's at least 1 move available
        selection = random.choice(selections)
        place(board, player, selection)
    return board

random_place(board, 2)

random.seed(1)
board = create_board()

for i in range(3):
    for player in [1, 2]: #here i will iterate each time for each player so that each player will move thrice
        random_place(board, player)

print(board)

def row_win(board, player):
    if np.any(np.all(board==player, axis=1)): # this checks if any row (axis=1) contains all positions equal to player.
        return True
    else:
        return False

print(row_win(board, 1))

def col_win(board, player):
    if np.any(np.all(board==player, axis=0)): # this checks if any column (axis=0) contains all positions equal to player.
        return True
    else:
        return False

col_win(board,1)

board[1,1] = 2
print(board)

def diag_win(board, player):
    if np.all(np.diag(board)==player) or np.all(np.diag(np.fliplr(board))==player):
        #np.diag returns the diagonal of the array
        #np.fliplr rearranges columns in reverse order (from left to right)
        return True
    else:
        return False

diag_win(board, 2)

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


sayHello("hey serg")  
# print(board)
# evaluate(board)