import sys
input = sys.stdin.readline

N = int(input())
eggs = [list(map(int,input().split())) for _ in range(N)]
answer = 0

def dfs(now):
    global answer
    if now == N :
        cnt = 0
        for egg in eggs:
            if egg[0] <= 0 :
                cnt += 1
        answer = max(answer,cnt)
        return

    if eggs[now][0] <= 0:
        dfs(now+1)
        return

    check = True
    for i in range(N):
        if now == i : continue
        if eggs[i][0] > 0 :
            check = False
            break

    if check:
        answer = max(answer, N-1)
        return


    for i in range(N):
        if now == i : continue
        if eggs[i][0] <= 0 : continue
        eggs[now][0] -= eggs[i][1]
        eggs[i][0] -= eggs[now][1]
        dfs(now+1)
        eggs[now][0] += eggs[i][1]
        eggs[i][0] += eggs[now][1]

dfs(0)
print(answer)