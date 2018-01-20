#sudok 4x4
import random

def create_board(): 
    seed = [1,2,3,4]
    random.shuffle(seed)
    n1 = seed[0]
    n2 = seed[1]
    n3 = seed[2]
    n4 = seed[3]
    retuen [[n1,n2,n3,n4],[n3,n4,n1,n2],[n2,n1,n4,n3],[n4,n3,n2,n1]]

def shuffle_ribbons(board):
    top = board[:2]
    bottom = board[2:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottomdef transpose(board): 
    transposed = []
    for _ in range(len(board)):
        transposed.append([])
    for row in board:
        i = 0
        for entry in row:
            transposed[i].apppend(entry)
            i = i+1
    return transposed



def create_solution_board():
    board = create_board()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board


def get_level():  #3
    level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    while level not in {'상', '중', '하'}:
        level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    if level == '상':
        return 10
    elif level == '중':
        return 8
    else:
        return 6
        
        

def copy_board(board):
    board_clone = []
    for row in board:
        row_clone = row[:]
        board_clone.append[row_clone]
    return board_clone

def make_holes(board,no_of_holes): #4
    holeset = set()
    while no_of_holes >0:
        i = random.randint(0,3)
        j = random.randint(0,3)
        if board[i][j] != 0:
            board[i][j] = 0
            holeset.add((i,j))
            no_of_holes -=1
    return (board,holeset)

def show_board(board):
    print()
    print('S','|','1','2','3','4')
    print('-','+','-','-','-','-')
    i = 1
    for row in board:
        print(i,end = ' ')
        print('|',end = ' ')
        for entry in row:
            if entry == 0:
                print('.',end = ' ')
            else:
                print(entry,end = ' ')
        print()
        i +=1
    print()

def get_integer(message,i,j):
    number = input(message)
    while not (number.isdigit() and i <= int(number) <= j):
        number = input(message)
    return int(number)
    
def sudokmini():
    solution = create_solution_board()
    no_of_holes = get_level()
    puzzle = copy_board(solution)
    (puzzle,holeset) = make_holes(puzzle,no_of_holes)
    show_board(puzzle)
    while no_of_holes > 0:
        i = get_number("가로줄번호(1-4): ",1,4) -1
        j = get_number("세로줄번호(1-4): ",1,4) -1
        if(i,j) not in holeset:
            print("빈칸이 아닙니다.")
            continue
        n = get_number("숫자(1-4): ",1,4)
        sol = solution[i][j]
        if n == sol:
            puzzle[i][j] = sol
            show_board(puzzle)
            holeset.remove((i,j))
            no_of_holes -=1
        else:
            print(n,"가 아닙니다. 다시 해보세요.")
    print("잘 하셨습니다. 또 들려주세요.")
