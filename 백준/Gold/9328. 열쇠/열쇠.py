from collections import deque

def bfs(y,x):
    global h, w, keys, fboard
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque()
    visit = [[0]*(w+2) for _ in range(h+2)]
    q.append([y, x])
    visit[y][x] = 1

    cnt = 0

    while q:
        nowy, nowx = q.popleft()
        for idx in range(4):
            nx = nowx + dx[idx]
            ny = nowy + dy[idx]

            if nx < 0 or nx >= w+2 or ny < 0 or ny >= h+2 : continue
            if visit[ny][nx] == 1 : continue
            if fboard[ny][nx].islower() :
                keys.append(fboard[ny][nx])
                visit = [[0] * (w + 2) for _ in range(h + 2)]
                fboard[ny][nx] = '.'
                q.append([ny,nx])

            elif fboard[ny][nx].isupper():
                if fboard[ny][nx].lower() in keys:
                    visit[ny][nx] = 1
                    fboard[ny][nx] = '.'
                    q.append([ny,nx])
                else : continue

            elif fboard[ny][nx] == '*' : continue
            elif fboard[ny][nx] == '.':
                visit[ny][nx] = 1
                q.append([ny,nx])
            elif fboard[ny][nx] == '$' :
                visit[ny][nx] = 1
                cnt += 1
                fboard[ny][nx] = '.'
                q.append([ny,nx])


    return cnt

T = int(input())
for tc in range(T):
    h,w = map(int,input().split())
    board = [list(map(str,input().strip())) for _ in range(h)]
    keys = list(map(str,input().strip()))

    if keys[0] == '0' :
        keys.pop()

    fboard = [['.']*(w+2) for _ in range(h+2)]
    for i in range(h):
        for j in range(w):
            fboard[i+1][j+1] = board[i][j]

    answer = bfs(0,0)

    print(answer)