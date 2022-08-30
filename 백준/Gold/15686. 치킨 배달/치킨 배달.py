from itertools import combinations

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

chicken = []
home = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken.append([i,j])
        elif board[i][j] == 1:
            home.append([i,j])

comb = combinations(chicken,M)
answerlist = []

for c in comb:
    #print(c)
    dist = []
    for hy,hx in home:
        mindist = 21e8
        for cy,cx in c:
            tmp = abs(hy-cy) + abs(hx-cx)
            if mindist > tmp:
                mindist = tmp
        dist.append(mindist)
    answerlist.append(sum(dist))

print(min(answerlist))