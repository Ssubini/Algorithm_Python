N,d,k,c = map(int,input().split())
sushi = [int(input()) for _ in range(N)]
Maxcnt = 0

tsushi = [0] * d
for i in range(k):
    tsushi[sushi[i%N]-1] += 1

tsushi[c-1] += 1

cnt = 0
for idx in range(d):
    if tsushi[idx] > 0 : cnt += 1

Maxcnt = cnt

for i in range(N-1):
    tsushi[sushi[i%N]-1] -= 1
    if tsushi[sushi[i%N]-1] == 0 : cnt-=1
    if tsushi[sushi[(i+k)%N]-1] == 0 : cnt += 1
    tsushi[sushi[(i+k)%N]-1] += 1

    Maxcnt = max(Maxcnt, cnt)

print(Maxcnt)
