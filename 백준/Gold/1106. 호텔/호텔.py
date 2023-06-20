C, N = map(int,input().split())
cost = [0]*N
value = [0]*N
for t in range(N):
    cost[t], value[t] = map(int,input().split())

dp = [21e8] * (C + 101)
dp[0] = 0

for i in range(N):
    for j in range(value[i], C + 101):
        dp[j] = min(dp[j-value[i]] + cost[i], dp[j])

print(min(dp[C:]))

