import sys
input = sys.stdin.readline
def find(c):
	if par[c] == c:
		return c
	else:
		par[c] = find(par[c])
	return par[c]
 
def union(a, b):
	a, b = find(a), find(b)
	par[max(a, b)] = min(a, b)
 
def check(a, b):
	return find(a) == find(b)
 
 
party = []
N, M = map(int,input().split())
know_truth = [False] * (N+1)
par = [i for i in range(N+1)]
t, *tp = map(int,input().split())
for i in range(t):
    know_truth[tp[i]] = True
 
for _ in range(M):
    p, *pp = map(int,input().split())
    party.append(pp)
    if p > 1:
        for i in range(p-1):       
            union(pp[i], pp[i+1])
 
for i in range(1, N+1):
    if know_truth[i]:
        know_truth[find(i)] = True
 
if t == 0:
    print(M)
    sys.exit(0)
else:
    answer = 0
    for i in party:
        tf = True
        for j in i:
            if know_truth[find(j)]:
                tf = False
        if tf:
            answer += 1
    print(answer)