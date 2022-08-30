N,M = map(int,input().split())
r,c,d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dd = [[-1,0],[0,1],[1,0],[0,-1]]

answer = 0
nowr = r
nowc = c
nowd = d
cnt = 0
while True:
    if board[nowr][nowc] == 0 :
        answer += 1
        board[nowr][nowc] = 2

    nxtd = (nowd+3)%4
    nxtr = nowr+dd[nxtd][0]
    nxtc = nowc+dd[nxtd][1]
    if board[nxtr][nxtc] == 0:
        nowd = nxtd
        nowr = nxtr
        nowc = nxtc
        cnt = 0
        continue
    else :
        if cnt < 4 :
            nowd = nxtd
            cnt += 1
        else :
            tmpd = (nowd+2)%4
            tmpr = nowr+dd[tmpd][0]
            tmpc = nowc+dd[tmpd][1]
            if board[tmpr][tmpc] == 1:
                break
            else :
                # nowd = tmpd  # 후진이라 방향은 안바뀜
                nowr = tmpr
                nowc = tmpc
                cnt = 0

print(answer)

