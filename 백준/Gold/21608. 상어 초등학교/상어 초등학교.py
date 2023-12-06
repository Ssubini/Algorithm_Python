import sys
from collections import defaultdict
input = sys.stdin.readline
fdict = defaultdict(list)

N = int(input())
friends = [list(map(int,input().split())) for _ in range(N*N)]
board = [[0]*N for _ in range(N)]
dy = [0,0,-1,1]
dx = [-1,1,0,0]

for friend in friends:
    now_student, like_friends = friend[0], friend[1:]
    fdict[now_student] = like_friends
    maxlike, maxempty = -1,-1
    maxy,maxx = 0,0
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0 : continue
            cntlike, cntempty = 0,0
            for idx in range(4):
                ny = i + dy[idx]
                nx = j + dx[idx]

                if ny < 0 or ny >= N or nx < 0 or nx >= N : continue
                if board[ny][nx] == 0 :
                    cntempty += 1
                if board[ny][nx] in like_friends:
                    cntlike += 1

            if maxlike < cntlike :
                maxy = i
                maxx = j
                maxlike = cntlike
                maxempty = cntempty
            elif maxlike == cntlike:
                if maxempty < cntempty :
                    maxy = i
                    maxx = j
                    maxempty = cntempty

    board[maxy][maxx] = now_student

answer = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        for idx in range(4):
            ny = i + dy[idx]
            nx = j + dx[idx]

            if ny < 0 or ny >= N or nx < 0 or nx >= N : continue
            if board[ny][nx] in fdict[board[i][j]]:
                cnt += 1

        if cnt == 1 :
            answer += 1
        elif cnt == 2 :
            answer += 10
        elif cnt == 3 :
            answer += 100
        elif cnt == 4 :
            answer += 1000


print(answer)


