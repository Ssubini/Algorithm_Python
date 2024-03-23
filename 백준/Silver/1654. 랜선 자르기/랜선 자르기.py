import sys
input = sys.stdin.readline

K, N = map(int,input().split())
lines = [int(input()) for _ in range(K)]

s = 1
e = max(lines)

while s <= e :
    mid = (s+e)//2
    cut = 0
    for line in lines:
        cut += line // mid
    
    if cut >= N:
        s = mid + 1
    else:
        e = mid - 1

print(e)


