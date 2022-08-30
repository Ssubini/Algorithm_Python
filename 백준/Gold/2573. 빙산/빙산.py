from collections import deque

def bfs():
    global board, N, M
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    count = 0
    while True:
        count += 1
        # 매 반복마다 visit 배열 만들기
        # 1 => 방문해야함
        visit = [[0]*M for _ in range(N)]
        fg = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] > 0 :
                    fg = 1
                    visit[i][j] = 1
        if fg == 0:
            return 0

        q = deque()

        flag = 0
        for i in range(N):
            for j in range(M):
                if visit[i][j] == 1 :
                    flag = 1
                    q.append([i, j])
                    visit[i][j] = 0
                    break
            if flag == 1: break

        while q:
            y,x = q.popleft()
            for idx in range(4):
                ny = y + dy[idx]
                nx = x + dx[idx]

                if ny < 0 or ny >=N or nx < 0 or nx >= M : continue
                if board[ny][nx] <= 0 and visit[ny][nx] != 2:
                    board[y][x] -= 1
                    visit[y][x] = 2
                elif visit[ny][nx] == 0 or visit[ny][nx] == 2: continue
                else :
                    visit[ny][nx] = 0
                    q.append([ny,nx])

        for i in range(N):
            if 1 in visit[i] :
                return count-1

    # bfs(count+1)

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
print(bfs())