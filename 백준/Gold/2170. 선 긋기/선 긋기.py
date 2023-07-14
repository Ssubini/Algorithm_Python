import sys
input = sys.stdin.readline
N = int(input())
dot = [list(map(int,input().split())) for _ in range(N)]
dot.sort(key = lambda x : (x[0],x[1]))
now = -1000000001
answer = 0
for d in dot:
    if d[0] >= now :
        answer += d[1]-d[0]
        now = d[1]
    else :
        if d[1] >= now :
            answer += d[1]-now
            now = d[1]
        else : continue

print(answer)
