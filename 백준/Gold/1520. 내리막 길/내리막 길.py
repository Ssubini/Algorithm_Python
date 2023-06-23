M, N = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(M)]
check = [[-1]*N for _ in range(M)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(y,x):
    if check[y][x] != -1 :
        return check[y][x]
    cnt = 0
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if nx < 0 or nx >= N or ny < 0 or ny >= M : continue
        if board[ny][nx] >= board[y][x]: continue
        cnt += dfs(ny,nx)

    check[y][x] = cnt
    return check[y][x]

check[-1][-1] = 1
print(dfs(0,0))
