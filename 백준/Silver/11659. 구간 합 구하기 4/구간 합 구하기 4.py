import sys
input = sys.stdin.readline
N, M = map(int,input().split())
nums = list(map(int,input().split()))
for i in range(1,N):
    nums[i] += nums[i-1]
nums = [0]+nums
for m in range(M):
    i, j = map(int,input().split())
    print(nums[j]-nums[i-1])