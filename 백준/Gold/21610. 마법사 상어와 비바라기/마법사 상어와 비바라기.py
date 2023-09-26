import sys
input = sys.stdin.readline

N, M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
moves = [list(map(int,input().split())) for _ in range(M)]


# 구름 이동
def move_cloud(d,s):
    global clouds
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    for c in range(len(clouds)):
        nowy,nowx = clouds[c][0]-1,clouds[c][1]-1
        ny = (nowy + dy[d-1]*s + N) % N + 1
        nx = (nowx + dx[d-1]*s + N) % N + 1
        clouds[c] = [ny,nx]

# 비
def rain():
    global A, clouds
    for cloud in clouds:
        A[cloud[0]-1][cloud[1]-1] += 1

# 물 복사 마법
def duplicate_water():
    global A, clouds
    dy = [-1,-1,1,1]
    dx = [-1,1,-1,1]
    for cloud in clouds:
        cnt = 0
        nowy, nowx = cloud
        for idx in range(4):
            ny = nowy + dy[idx]
            nx = nowx + dx[idx]
            if ny < 1 or ny >= N+1 or nx < 1 or nx >= N+1 : continue
            if A[ny-1][nx-1] > 0 :
                cnt += 1

        A[nowy-1][nowx-1] += cnt

# 구름생성
def make_cloud():
    global A, clouds
    check = [[0]*N for _ in range(N)]
    new_clouds = []
    for cloud in clouds:
        check[cloud[0]-1][cloud[1]-1] = -1

    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and check[i][j] != -1 :
                new_clouds.append([i+1,j+1])
                A[i][j] -= 2

    return new_clouds

clouds = [[N,1],[N,2],[N-1,1],[N-1,2]]
cnt = 1
for m in moves:
    cnt += 1
    move_cloud(m[0],m[1])
    rain()
    duplicate_water()
    clouds = make_cloud()

answer = 0
for i in range(N):
    for j in range(N):
        answer += A[i][j]

print(answer)