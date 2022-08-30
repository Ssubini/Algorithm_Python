board = [list(map(int,input().split())) for _ in range(9)]
zero = [(i,j) for i in range(9) for j in range(9) if board[i][j] == 0]

def check(x,y):
    key = [1,2,3,4,5,6,7,8,9]
    # 가로 세로
    for i in range(9):
        if board[x][i] in key:
            key.remove(board[x][i])
        if board[i][y] in key:
            key.remove(board[i][y])

    x1 = x//3
    y1 = y//3
    # 3x3 box
    for i in range(x1*3, x1*3+3):
        for j in range(y1*3, y1*3+3):
            if board[i][j] in key:
                key.remove(board[i][j])

    return key


def sdc(n):
    if n == len(zero):
        for i in range(9):
            for j in range(9):
                print(board[i][j],end=' ')
            print()
        exit()

    i,j = zero[n]
    for k in check(i,j):
        board[i][j] = k
        sdc(n+1)
        board[i][j] = 0

sdc(0)