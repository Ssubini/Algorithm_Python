from collections import deque
from copy import deepcopy

def bfs():
    global answer
    cboard = deepcopy(board)
    safe = 0
    q = deque()
    for i in range(N):
        for j in range(M):
            if cboard[i][j] == 2:
                q.append([i, j])

    while q:
        nowy, nowx = q.popleft()
        for idx in range(4):
            ny = nowy + dy[idx]
            nx = nowx + dx[idx]

            if ny < 0 or ny >= N or nx < 0 or nx >= M: continue
            if cboard[ny][nx] == 0:
                cboard[ny][nx] = 2
                q.append([ny, nx])

    for i in cboard:
        for j in i:
            if j == 0:
                safe += 1

    answer = max(answer, safe)


def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(cnt + 1)
                board[i][j] = 0


N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
answer = 0
wall(0)
print(answer)

