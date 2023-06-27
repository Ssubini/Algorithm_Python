from collections import deque
chain = [deque(list(input())) for _ in range(4)]
k = int(input())

def left(now, l, dir):
    if l < 0:
        return
    if chain[now][6] != chain[l][2]:
        left(l, l-1, -dir)
        chain[l].rotate(-dir)

def right(now, r, dir):
    if r > 3:
        return
    if chain[now][2] != chain[r][6]:
        right(r, r+1, -dir)
        chain[r].rotate(-dir)

for _ in range(k):
    num, dir = map(int, input().split())
    left(num-1, num-2, dir)
    right(num-1, num, dir)
    chain[num-1].rotate(dir)

answer = 0
for i in range(4):
    if chain[i][0] == "1":
        answer += (2**i)

print(answer)