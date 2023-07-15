import sys
import heapq
input = sys.stdin.readline

N = int(input())
cls = [list(map(int,input().split())) for _ in range(N)]
cls.sort(key = lambda x : x[0])

q = []
for c in cls:
    if q and q[0] <= c[0]:
        heapq.heappop(q)
    heapq.heappush(q,c[1])

print(len(q))
