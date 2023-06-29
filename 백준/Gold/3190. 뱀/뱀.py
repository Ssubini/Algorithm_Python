from collections import deque
N = int(input())
K = int(input())
board = [[-1]*N for _ in range(N)]
for _ in range(K):
    y,x = map(int,input().split())
    board[y-1][x-1] = 5
L = int(input())
headdir = deque([list(map(str,input().split())) for _ in range(L)])
board[0][0] = 0
time = 0
d = [[0,1],[1,0],[0,-1],[-1,0]]
snake = deque()
# head = [0,0]
# tail = [0,0]
snake.append([0,0])

while True:
    time += 1
    head = snake[0]
    nowdir = board[head[0]][head[1]]
    ny = head[0]+d[board[head[0]][head[1]]][0]
    nx = head[1]+d[board[head[0]][head[1]]][1]

    if ny < 0 or nx < 0 or ny >= N or nx >= N : break
    if board[ny][nx] == 0 or board[ny][nx] == 1 or board[ny][nx] == 2 or board[ny][nx] == 3 : break
    if board[ny][nx] == -1:
        tail = snake.pop()
        board[tail[0]][tail[1]] = -1

    if headdir and time == int(headdir[0][0]):
        t, hd = headdir.popleft()
        if hd == 'L':
            board[ny][nx] = (nowdir+4-1)%4
        else :
            board[ny][nx] = (nowdir+1)%4
    else :
        board[ny][nx] = nowdir
    snake.appendleft([ny,nx])

print(time)
