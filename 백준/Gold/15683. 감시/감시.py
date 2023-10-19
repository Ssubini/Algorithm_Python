import sys
import copy
input = sys.stdin.readline

N, M = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(N)]
cctv = []
empty = 0
answer = N*M
ct = [[[[0,1]],[[0,-1]],[[1,0]],[[-1,0]]],
      [[[0,1],[0,-1]],[[1,0],[-1,0]]],
      [[[0,1],[1,0]],[[1,0],[0,-1]],[[0,-1],[-1,0]],[[-1,0],[0,1]]],
      [[[0,-1],[1,0],[-1,0]],[[0,1],[1,0],[-1,0]],[[0,1],[0,-1],[-1,0]],[[0,1],[0,-1],[1,0]]],
      [[[0,1],[0,-1],[1,0],[-1,0]]]]

ct1 = [[[0,1]],[[0,-1]],[[1,0]],[[-1,0]]]
ct2 = [[[0,1],[0,-1]],[[1,0],[-1,0]]]
ct3 = [[[0,1],[1,0]],[[1,0],[0,-1]],[[0,-1],[-1,0]],[[-1,0],[0,1]]]
ct4 = [[[0,-1],[1,0],[-1,0]],[[0,1],[1,0],[-1,0]],[[0,1],[0,-1],[-1,0]],[[0,1],[0,-1],[1,0]]]
ct5 = [[[0,1],[0,-1],[1,0],[-1,0]]]
for i in range(N):
    for j in range(M):
        if room[i][j] == 0 :
            empty += 1
        elif room[i][j] != 6 :
            cctv.append([i,j,room[i][j]])

def dfs(level, state) :
    global answer
    if level == len(cctv):
        emptycnt = 0
        for i in range(N):
            for j in range(M):
                if state[i][j] == 0 :
                    emptycnt += 1

        answer = min(answer, emptycnt)
        return

    cctvy, cctvx, cctvnum = cctv[level]

    for idx in range(len(ct[cctvnum-1])):
        nowstate = copy.deepcopy(state)
        for inneridx in range(len(ct[cctvnum-1][idx])):
            dy,dx = ct[cctvnum-1][idx][inneridx]
            cnt = 1
            while True:
                ny = cctvy + dy * cnt
                nx = cctvx + dx * cnt
                if ny < 0 or nx < 0 or ny >= N or nx >= M: break
                if nowstate[ny][nx] == 6 : break
                if nowstate[ny][nx] == 0:
                    nowstate[ny][nx] = -1
                cnt += 1
        dfs(level + 1, nowstate)

dfs(0,room)

print(answer)