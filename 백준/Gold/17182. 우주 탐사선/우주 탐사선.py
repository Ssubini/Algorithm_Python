import math
N, K = map(int,input().split())
times = [list(map(int,input().split())) for _ in range(N)]
visited = [0]*N
visited[K] = 1
answer = math.inf

for i in range(N):
    for j in range(N):
        for k in range(N):
            times[j][k] = min(times[j][k], times[j][i] + times[i][k])


def dfs(level, now, cost):
    global answer

    if level == N:
        answer = min(answer, cost)
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(level+1, i, cost + times[now][i])
            visited[i] = 0

dfs(1, K, 0)
print(answer)