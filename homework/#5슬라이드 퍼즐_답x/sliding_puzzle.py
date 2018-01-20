def sliding_puzzle():
    board = create_init_board()
    goal = set_goal_board()
    empty = (0,0)
    #비어있는 장소를 저장
    while True:
        print_board(board)
        if board ==goal:
            print("Confratulations!")
            break
        num = get_number()
        if num ==0:
            break
        pos = find_position(num,board)
        empty = move(pos,empty,board,num)
    print("Please come again.")


def create_init_board():
    return[ ['   ',15,14,13],[12,11,10,9],[8,7,6,5],[4,3,2,1]]

def set_goal_board():
    return [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,'   ']]

def get_number():
    x = input("Type the number you want to move(Type 0  to quit) ")
    while not ((len(x) == 1 or len(x) == 2) and x.isdigit() and 0 <= int(x) <= 15):
        x = input("Type the number you want to move(Type 0  to quit) ")
    return int(x)

def print_board(board):
        for x in range(0,4):
            for y in range(0,4):
                if len(str(board[x][y])) == 1:
                    print(str(board[x][y]).rjust(2),end=' ')
                else:
                    print(str(board[x][y]).rjust(1),end=' ')
            print()

#위치를 pos변수에 저장
def find_position(num,board):
    for x in range(0,4):
        for y in range(0,4):
            if board[x][y] == num:
                return (x,y)
    
#이동가능한지 확인하고 empty좌표 갱신
def move(pos,empty,board,num):
    if pos ==(empty[0]-1,empty[1]) or pos ==(empty[0]+1,empty[1]) or pos ==(empty[0],empty[1]-1) or pos ==(empty[0],empty[1]+1):
        board[empty[0]][empty[1]] = num
        board[pos[0]][pos[1]] = '   '
        return pos
    else:
        print("Can 't move! Try again.")
        return empty
# empty = pos 문을 실행하지 못한다.??
