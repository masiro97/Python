def sliding_puzzle():
    board = create_init_board()
    goal = set_goal_board()
    empty = (0,0)
    while True:
        print_board(board)
        if board == goal:
            print("Congratulation!")
            break
        num = get_number()
        if num == 0:
            break
        pos  = find_position(num,board)
        (empty,board) = move(pos,empty,board)
    print("Please come again.")

def create_init_board():
    return [[0,15,14,13],[12,11,10,9],[8,7,6,5],[4,3,2,1]]

def print_board(board):
    for row in board:
        for num in row:
            if num == 0:
                print("  ",end = ' ')
            elif 10 <= num <= 15:
                print(num,end = ' ')
            else:
                print(str(num).rjust(2),end = ' ')
        print()
        
def get_number():
    num = input("Type the number you want to move (Type 0 to quit): ")
    while not(num.isdigit() and 0 <= int(num) <= 15):
        num = input("Type the number you want to move (Type 0 to quit): ")
    return int(num)


def find_position(num,board):
    for i in range(4):
        for j in range(4):
            if num == board[i][j]:
                return (i,j)

def move(pos,empty,board):
    (x,y) = pos
    if empty == (x-1,y) or empty == (x+1,y) or \
       empty == (x,y-1) or empty == (x,y+1):
        board[empty[0]][empty[1]] = board[x][y]
        board[x][y] = 0
        return (pos, board)
    else:
        print("Can't move! Try again.")
        return (empty,board)

    
            
