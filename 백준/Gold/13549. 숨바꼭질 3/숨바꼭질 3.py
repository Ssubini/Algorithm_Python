from collections import deque

N, K = map(int,input().split())
board = [-1]*100001
q = deque()
q.append(N)
board[N] = 0

while q:
    now = q.popleft()

    if now == K :
        print(board[now])
        break

    for i in range(3):
        if i == 1 :
            if now-1 < 0 or now-1 > 100000 : continue
            if board[now-1] != -1 : continue
            board[now-1] = board[now] + 1
            q.append(now-1)
        elif i == 2:
            if now+1 < 0 or now+1 > 100000: continue
            if board[now + 1] != -1: continue
            board[now+1] = board[now] + 1
            q.append(now+1)
        elif i == 0:
            if now*2 < 0 or now*2 > 100000 : continue
            if board[now*2] != -1 : continue
            board[now*2] = board[now]
            q.append(now*2)

