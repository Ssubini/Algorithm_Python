import heapq
N = int(input())
M = int(input())
connect = [[] for _ in range(N+1)]
for _ in range(M):
    startcity,endcity,price = map(int,input().split())
    connect[startcity].append((price,endcity))

start,end = map(int,input().split())
inf = int(21e8)
result = [inf]*(N+1)

def dijkstra(start):
    result[start] = 0
    heap = []
    heapq.heappush(heap,(0,start))

    while heap:
        directcost, ky = heapq.heappop(heap)

        if directcost > result[ky]:
            continue

        for i in connect[ky]:
            skdcost = directcost + i[0]

            if skdcost < result[i[1]]:
                result[i[1]] = skdcost
                heapq.heappush(heap,(skdcost,i[1]))

dijkstra(start)
print(result[end])

