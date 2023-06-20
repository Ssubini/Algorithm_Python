from collections import defaultdict
for t in range(3):
    N = int(input())
    coins = defaultdict(int)
    total = 0
    for i in range(N):
        price, nums = map(int,input().split())
        coins[price] = nums
        total += price * nums

    if total % 2 == 1 :
        print(0)
        continue

    target = total // 2
    dp = [0] * (target+1)
    dp[0] = 1
    answer = 0
    for coin in coins.keys():
        for j in range(target, coin-1, -1):
            if dp[j-coin]:
                for k in range(coins[coin]):
                    if j + coin * k <= target :
                        dp[j + coin * k] = 1
                    else :
                        break
        if dp[-1] == 1:
            answer = 1
            break

    print(answer)
