from collections import defaultdict
N, K = map(int,input().split())
A = list(map(int,input().split()))
count = defaultdict(int)
s,e = 0,0
answer = 0

while e < N:
    if count[A[e]] >= K:
        count[A[s]] -= 1
        s += 1
    else :
        count[A[e]] += 1
        e += 1
        answer = max(answer, e-s)
print(answer)
