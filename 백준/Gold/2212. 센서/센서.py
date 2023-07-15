import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensor = list(map(int,input().split()))
sensor.sort()

if K >= N :
    print(0)
else :
    d = []
    for i in range(1,N):
        d.append(sensor[i]-sensor[i-1])

    d.sort(reverse = True)
    for i in range(K-1):
        d.pop(0)

    print(sum(d))