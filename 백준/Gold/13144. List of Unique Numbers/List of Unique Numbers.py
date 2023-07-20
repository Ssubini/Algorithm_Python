N = int(input())
arr = list(map(int,input().split()))
check = [0]*100001
s, e = 0,0
answer = 0
while s < N and e < N :
    if check[arr[e]] == 0 :
        check[arr[e]] = 1
        e += 1
        answer += (e-s)
    else :
        check[arr[s]] = 0
        s += 1

print(answer)