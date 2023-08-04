import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, K = map(int,input().split())
    houses = list(map(int,input().split()))
    if N == M :
        if sum(houses) < K : print(1)
        else: print(0)
        continue
    houses += houses[:M]
    answer = 0
    now = sum(houses[0:M])
    for i in range(1,len(houses)-M+1):
        if now < K :
            answer += 1
        now -= houses[i-1]
        now += houses[i+M-1]

    print(answer)