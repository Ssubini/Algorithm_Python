import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

board = [list(input().rstrip()) for _ in range(5)]
answer = 0
position = [(i,j) for i in range(5) for j in range(5)]
combs = combinations(position,7)
dy = [0,1,0,-1]
dx = [1,0,-1,0]

for comb in combs:
    cnts = 0
    for y,x in comb:
        if board[y][x] == 'S' :
            cnts += 1
    if cnts < 4 : continue

    q = deque()
    sy,sx = comb[0]
    q.append(comb[0])
    visits = [False]*7
    visits[0] = True

    while q:
        nowy, nowx = q.popleft()
        for idx in range(4):
            ny = nowy + dy[idx]
            nx = nowx + dx[idx]
            if ny < 0 or ny >= 5 or nx < 0 or nx >= 5 : continue
            if (ny,nx) in comb:
                cidx = comb.index((ny,nx))
                if not visits[cidx] :
                    visits[cidx] = True
                    q.append((ny,nx))

    if False in visits:
        continue
    answer += 1

print(answer)
