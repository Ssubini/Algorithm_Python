N, M, K = map(int,input().split())
sticker = []
for _ in range(K):
    R, C = map(int,input().split())
    tmp = []
    for i in range(R):
        tmp.append(list(map(int,input().split())))
    sticker.append(tmp)

notebook = [[0]*M for _ in range(N)]

def rotate(board):
    r, c = len(board), len(board[0])
    r_board = [[0]*r for _ in range(c)]

    for i in range(c):
        for j in range(r):
            r_board[i][j] = board[r-j-1][i]

    return r_board

def check(y,x,s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if notebook[y+i][x+j] == 1 and s[i][j] == 1 :
                return False
    return True

def attach(y,x,s):
    global notebook
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 1:
                notebook[y+i][x+j] = 1

for k in range(K):
    nowsticker = sticker[k]
    flag = False
    for t in range(4):
        for i in range(N-len(nowsticker)+1):
            for j in range(M-len(nowsticker[0])+1):
                if check(i,j,nowsticker):
                    attach(i,j,nowsticker)
                    flag = True
                    break
            if flag : break
        if flag : break
        else:
            nowsticker = rotate(nowsticker)

answer = 0
for i in range(N):
    for j in range(M):
        if notebook[i][j] == 1 : answer += 1

print(answer)