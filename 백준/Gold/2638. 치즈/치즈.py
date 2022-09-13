from collections import deque
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
count = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]

cheeze = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            cheeze += 1

while cheeze != 0:
    visit = [[0] * M for _ in range(N)]
    q = deque()
    q.append([0,0])
    visit[0][0] = 1

    while q:
        nowy, nowx = q.popleft()

        for idx in range(4):
            ny = nowy + dy[idx]
            nx = nowx + dx[idx]

            if ny < 0 or ny >= N or nx < 0 or nx >= M : continue
            if board[ny][nx] >= 1 :
                board[ny][nx] += 1
            if visit[ny][nx] == 0 and board[ny][nx] == 0:
                visit[ny][nx] = 1
                q.append([ny,nx])

    for i in range(N):
        for j in range(M):
            if board[i][j] >= 3:
                board[i][j] = 0
                cheeze -= 1
            elif board[i][j] == 2:
                board[i][j] = 1
    count += 1

print(count)