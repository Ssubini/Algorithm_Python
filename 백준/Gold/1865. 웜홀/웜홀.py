T = int(input())
for tc in range(T):
    N,M,W = map(int,input().split())
    road = []
    for _ in range(M):
        S, E, T = map(int,input().split())
        road.append([S, E, T])
        road.append([E, S, T])
    for _ in range(W):
        S, E, T = map(int,input().split())
        road.append([S, E, T*(-1)])

    flag = False

    time = [21e8] * (N+1)

    for i in range(N):
        for cur, nxt, cost in road:
            if time[nxt] > time[cur] + cost:
                time[nxt] = time[cur] + cost
                if i == N-1:
                    flag = True
                    break

    if flag:
        print('YES')
    else:
        print('NO')
