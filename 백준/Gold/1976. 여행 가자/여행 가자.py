from collections import deque
N = int(input())
M = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
t = list(map(int,input().split()))

visit = [False]*N
q = deque()
q.append(t[0]-1)
visit[t[0]-1] = True
while q:
    now = q.popleft()
    for i in range(len(board[now])):
        if visit[i] : continue
        if board[now][i] == 1:
            visit[i] = True
            q.append(i)

answer = 'YES'
for i in t:
    if not visit[i-1] :
        answer = 'NO'
        break

print(answer)