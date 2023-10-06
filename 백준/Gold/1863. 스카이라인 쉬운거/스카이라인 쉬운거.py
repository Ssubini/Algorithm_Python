import sys
input = sys.stdin.readline

N = int(input())
answer = 0
stack = []
checkzero = False

for _ in range(N):
    x,y = map(int,input().split())
    if y == 0 : checkzero = True
    while True:
        if not stack:
            stack.append(y)
            break
        else:
            if stack[-1] > y:
                stack.pop()
                answer += 1
                continue
            elif stack[-1] == y:
                break
            else:
                stack.append(y)
                break


answer += len(stack)
if checkzero : answer -= 1
print(answer)