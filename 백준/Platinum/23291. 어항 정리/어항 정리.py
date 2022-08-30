import copy
N, K = map(int,input().split())
nowfish = list(map(int,input().split()))


# 물고기 추가
def addFish():
    global board
    minfish = min(board[N-1])
    for i in range(len(board[N-1])):
        if board[N-1][i] == minfish:
            board[N-1][i] += 1

# 어항 쌓기
def putOn(board):

    idx = 0
    height = 1
    width = 1
    cnt = 1
    while True:
        nboard = [[-1] * N for _ in range(N)]
        if idx+height > N-1 : break

        tmp = [[0]*height for _ in range(width)]

        for w in range(width):
            for h in range(height):
                tmp[width-w-1][h] = board[(N)-h-1][idx-w]

        for i in range(idx+1,N):
            nboard[N-1][i] = board[N-1][i]

        for w in range(width):
            for h in range(height):
                nboard[N-1-width+w][h+idx+1] = tmp[w][h]

        board = copy.deepcopy(nboard)

        idx += height
        width = height
        if cnt % 2 == 1 : height += 1
        cnt += 1

    return board

# 비교 후 물고기 나누기
def share():
    dx = [0,1]
    dy = [1,0]
    nboard = copy.deepcopy(board)
    for i in range(N):
        for j in range(N):
            for idx in range(2):
                nx = j + dx[idx]
                ny = i + dy[idx]

                if nx >= N or ny >= N : continue
                if board[i][j] == -1 or board[ny][nx] == -1 : continue
                if board[i][j] >= board[ny][nx] :
                    tmp = (board[i][j] - board[ny][nx]) // 5
                    if tmp > 0:
                        nboard[i][j] -= tmp
                        nboard[ny][nx] += tmp
                else :
                    tmp = (board[ny][nx] - board[i][j]) // 5
                    if tmp > 0:
                        nboard[i][j] += tmp
                        nboard[ny][nx] -= tmp

    return nboard

# 펼치기
def oneLine():
    nboard = [[-1] * N for _ in range(N)]
    idx = 0
    for j in range(N):
        for i in range(N):
            if board[N-1-i][j] != -1:
                nboard[N-1][idx] = board[N-1-i][j]
                idx += 1

    return nboard

# 반씩 섞기
def halfShake():
    global board
    nboard = [[-1] * N for _ in range(N)]
    for i in range(N//2):
        nboard[N-1][i] = board[N-1][N//2+i]
        nboard[N-2][i] = board[N-1][N//2-1-i]

    board = copy.deepcopy(nboard)
    nboard = [[-1] * N for _ in range(N)]
    for i in range((N//2)//2):
        nboard[0][i] = board[N-1][(N//2)//2-1-i]
        nboard[1][i] = board[N-2][(N//2)//2-1-i]
        nboard[2][i] = board[N-2][(N//2)//2+i]
        nboard[3][i] = board[N-1][(N//2)//2+i]

    return nboard

answer = 0
while True:
    board = [[-1] * N for _ in range(N)]
    board[N-1] = copy.deepcopy(nowfish)
    check = max(board[N-1]) - min(board[N-1])
    if check <= K : break
    answer += 1
    addFish()
    board = putOn(board)
    board = share()
    board = oneLine()
    board = halfShake()
    board = share()
    board = oneLine()
    nowfish = copy.deepcopy(board[N-1])

print(answer)