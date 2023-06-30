import sys
input = sys.stdin.readline

N = int(input())
tower = list(map(int,input().split()))
answer = [0]*N
stack = []
for t in range(len(tower)):
    while stack:
        if stack[-1][1] > tower[t] :
            answer[t] = stack[-1][0]
            break
        else:
            stack.pop()
    stack.append([t+1,tower[t]])

print(' '.join(map(str,answer)))
