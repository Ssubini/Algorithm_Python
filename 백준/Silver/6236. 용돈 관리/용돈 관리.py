N, M = map(int,input().split())
money = [int(input()) for _ in range(N)]
s, e = min(money), sum(money)

while s <= e:
    cnt = 1
    mid = (s+e)//2
    now = mid
    for i in range(N):
        if now < money[i]:
            now = mid
            cnt += 1
        now -= money[i]

    if cnt > M or mid < max(money):
        s = mid + 1
    else :
        e = mid - 1
        k = mid

print(k)
