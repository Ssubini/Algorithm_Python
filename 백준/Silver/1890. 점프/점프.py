N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1
answer = 0

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1 :
            answer = dp[i][j]
            break
        
        if j + board[i][j] < N :
            dp[i][j+board[i][j]] += dp[i][j]
        
        if i + board[i][j] < N :
            dp[i+board[i][j]][j] += dp[i][j]

print(answer)