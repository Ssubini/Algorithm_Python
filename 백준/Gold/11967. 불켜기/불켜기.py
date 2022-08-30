from collections import deque

N, M = map(int,input().split())
swc = [list(map(int,input().split())) for _ in range(M)]
board = [[0]*(N+1) for _ in range(N+1)]
visit = [[0]*(N+1) for _ in range(N+1)]

q = deque()
q.append([1,1])
visit[1][1] = 1
board[1][1] = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer = 1

while q:
    nowy, nowx = q.popleft()

    for i in range(M):
        if swc[i][0] == nowx and swc[i][1] == nowy :
            if board[swc[i][3]][swc[i][2]] == 0:
                board[swc[i][3]][swc[i][2]] = 1
                answer += 1

                for idx in range(4):
                    nx = swc[i][2] + dx[idx]
                    ny = swc[i][3] + dy[idx]

                    if nx < 1 or nx >= (N + 1) or ny < 1 or ny >= (N + 1) : continue
                    if visit[ny][nx] != 0 :
                        q.append([ny,nx])


    for idx in range(4):
        nx = nowx + dx[idx]
        ny = nowy + dy[idx]

        if nx < 1 or nx >= N+1 or ny < 1 or ny >= N+1 : continue
        if visit[ny][nx] != 0 : continue
        if board[ny][nx] == 0 : continue
        visit[ny][nx] = 1
        q.append([ny,nx])

print(answer)