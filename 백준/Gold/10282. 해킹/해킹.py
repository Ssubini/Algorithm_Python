import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    dist[start] = 0

    while q:
        distance, cur = heapq.heappop(q)
        if dist[cur] > distance: continue

        for nxt, dst in graph[cur]:
            cost = distance + dst
            if cost < dist[nxt]:
                dist[nxt] = cost
                heapq.heappush(q, (cost, nxt))


T = int(input())
for tc in range(T):
    n,d,c = map(int,input().split())
    graph = [[] for _ in range(n+1)]

    for i in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((a,s))

    INF = 21e8
    dist = [INF]*(n+1)
    result = []

    dijkstra(c)

    for d in dist:
        if d < INF:
            result.append(d)

    print(len(result), max(result))