import heapq
V,E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for i in range(E):
    s, e, w = map(int,input().split())
    graph[s].append((e,w))

INF = 21e8
dist = [INF for _ in range(V+1)]
dist[K] = 0
q = []
heapq.heappush(q,(0,K))

while q:
    distance, cur = heapq.heappop(q)
    if distance > dist[cur] : continue
    for nxt, dst in graph[cur]:
        cost = distance + dst
        if cost < dist[nxt]:
            dist[nxt] = cost
            heapq.heappush(q, (cost, nxt))

for i in range(1,V+1):
    if dist[i] >= INF:
        print('INF')
    else:
        print(dist[i])