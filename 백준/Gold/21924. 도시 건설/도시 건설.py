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
	par[max(a,b)] = min(a,b)
 
def check(a, b):
	return find(a) == find(b)
 
N, M = map(int,input().split())
par = [i for i in range(N+1)]
build = []
total_cost = 0
for _ in range(M):
    a, b, c = map(int,input().split())
    build.append((c, a, b))
    total_cost += c
build.sort()
 
cost = 0
for c, a, b in build:
    if not check(a, b):
        cost += c
        union(a, b)
 
tmp = 0
for i in range(1, N+1):
    if par[i] == i:
        tmp += 1
 
if tmp >= 2:
    print(-1)
else:
    print(total_cost - cost)
