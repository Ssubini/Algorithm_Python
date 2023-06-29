from collections import deque

a,b,c = map(int,input().split())
total = a+b+c
answer = 0
visit = [[0]*(total+1) for _ in range(total+1)]
if total % 3 != 0 :
    answer = 0
else :
    q = deque()
    q.append([a,b])
    visit[a][b] = True
    while q:
        x,y = q.popleft()
        z = total - x - y
        if x == y == z :
            answer = 1
            break

        for a,b in (x,y),(y,z),(x,z):
            if a < b :
                b -= a
                a += a
            elif a > b :
                a -= b
                b += b
            else :
                continue

            c = total - a - b
            x = min(a,b,c)
            y = max(a,b,c)

            if visit[x][y] == 0:
                q.append([x,y])
                visit[x][y] = 1

print(answer)