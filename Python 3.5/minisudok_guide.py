#sudok 4x4
import random

def create_board(): #1
    seed = [1,2,3,4]
    random.shuffle(seed)
    #...

def shuffle_ribbons(board):
    top = board[:2]
    bottom = board[2:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottom

def transpose(board): #2
    transposed = []
    for _ in range(len(board)):
        transposed.append([])

    #...
    return transposed

def create_solution_board():
    board = create_board()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board


def get_level():  #3
    #...

def copy_board(board):
    board_clone = []
    for row in board:
        row_clone = row[:]
        board_clone.append[row_clone]
    return board_clone

def make_holes(board,no_of_holes): #4
    holeset = set()
    pass
    return (board,holeset)

def show_board(board): #5
    pass

def get_integet(message,i,j): #6
    return 0
