import random

def sudokmini():
    solution = create_solution_board()
    no_of_holes = get_level()
    puzzle = copy_board(solution)
    (puzzle,holeset) = make_holes(puzzle,no_of_holes)
    show_board(puzzle)
    while no_of_holes > 0:
        i = get_interger("가로줄번호(1-4): ",1,4) -1
        j = get_interger("세로줄번호(1-4): ",1,4) -1
        if (i,j) not in holeset:
            print("빈칸이 아닙니다.")
            continue
        n = get_interger("숫자(1-4): ",1,4)
        sol = solution[i][j]
        if n == sol:
            puzzle[i][j] = sol
            show_board(puzzle)
            holeset.remove((i,j))
            no_of_holes -= 1
        else:
            print(n,"가 아닙니다. 다시 해보세요.")
    print("잘 하셨습니다. 또 들려주세요.")
        
def make_holes(puzzle,no_of_holes):
    holeset = set()
    while no_of_holes >0:
        (i,j) = (random.randint(0,3),random.randint(0,3))
        while puzzle[i][j] == '.':
            (i,j) = (random.randint(0,3),random.randint(0,3))
        puzzle[i][j] = '.'
        holeset.add((i,j))
        no_of_holes = no_of_holes -1
    return (puzzle,holeset)    

def create_solution_board():
    board = create_board()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board


def copy_board(board):
    board_clone = []
    for row in board :
        row_clone = row[:]
        board_clone.append(row_clone)
    return board_clone


def create_board():
    seed = [1,2,3,4]
    random.shuffle(seed)
    board = [[seed[0],seed[1],seed[2],seed[3]],[seed[2],seed[3],seed[0],seed[1]],[seed[1],seed[0],seed[3],seed[2]],[seed[3],seed[2],seed[1],seed[0]]]
    return board

def get_level():
    level = input("난이도 (상, 중, 하) 중에서 하나 선택하여 입력: ")
    while level not in {'상','중','하'}:
        level = input("난이도 (상, 중, 하) 중에서 하나 선택하여 입력: ")
    if level == '상':
        return 10
    elif level ==  '중':
        return 8
    elif level == '하':
        return 6
    
def get_interger(str,a,b):
    x = input(str)
    while not (len(x) == 1 and x.isdigit() and a <= int(x) <= b):
        x = input(str)
    return int(x)


def show_board(puzzle):
    board = [['S','|',1,2,3,4],['-','+','-','-','-','-'],[1,'|',puzzle[0][0],puzzle[0][1],puzzle[0][2],puzzle[0][3]],[2,'|',puzzle[1][0],puzzle[1][1],puzzle[1][2],puzzle[1][3]],[3,'|',puzzle[2][0],puzzle[2][1],puzzle[2][2],puzzle[2][3]],[4,'|',puzzle[3][0],puzzle[3][1],puzzle[3][2],puzzle[3][3]]]
    for m in range(0,6):
        for n in range(0,6):
            print(board[m][n],end = ' ')
        print()



def shuffle_ribbons(board) :
    top = board[:2]
    bottom = board[2:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottom


def transpose(board) :
    transposed = []  
    for _ in range(len(board)):
        transposed.append([])
    for x in range (0,4):
        for y in range(0,4):
            transposed[x].append(board[x][y])
    
    return transposed



    
