import sys
from collections import deque
input = sys.stdin.readline

dy = [1,0,-1,0]
dx = [0,1,0,-1]

N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(M)]

# 벽 표시
realboard = [[[False]*4 for _ in range(N)]for _ in range(M)]
for i in range(M):
    for j in range(N):
        tmp = board[i][j]
        if tmp // 8 == 1 :
            realboard[i][j][0] = True
        tmp %= 8
        if tmp // 4 == 1 :
            realboard[i][j][1] = True
        tmp %= 4
        if tmp // 2 == 1 :
            realboard[i][j][2] = True
        if tmp % 2 == 1 :
            realboard[i][j][3] = True

# 방 개수와 넓이
visit = [[-1]*N for _ in range(M)]
max_size = -1
room_number = 0
room_size = [0]

for i in range(M):
    for j in range(N):
        if visit[i][j] == -1:
            room_number += 1
            q = deque()
            q.append([i,j])
            visit[i][j] = room_number
            cnt = 1
            while q:
                nowy, nowx = q.popleft()

                for idx in range(4):
                    if not realboard[nowy][nowx][idx] :
                        ny = nowy + dy[idx]
                        nx = nowx + dx[idx]

                        if ny < 0 or nx < 0 or ny >= M or nx >= N : continue
                        if visit[ny][nx] != -1 : continue
                        cnt += 1
                        visit[ny][nx] = room_number
                        q.append([ny,nx])

            max_size = max(max_size, cnt)
            room_size.append(cnt)

max_merge_size = 0

for i in range(M):
    for j in range(N):
        if i+1 < M and visit[i][j] != visit[i+1][j] :
            max_merge_size = max(max_merge_size, room_size[visit[i][j]] + room_size[visit[i+1][j]])
        if j+1 < N and visit[i][j] != visit[i][j+1]:
            max_merge_size = max(max_merge_size, room_size[visit[i][j]] + room_size[visit[i][j+1]])

print(room_number)
print(max_size)
print(max_merge_size)