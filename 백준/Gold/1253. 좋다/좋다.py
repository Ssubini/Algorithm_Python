N = int(input())
A = list(map(int,input().split()))
A.sort()
answer = 0

for i in range(N):
    s, e = 0, len(A)-1

    while s != e :
        tmp = A[s] + A[e]
        if tmp == A[i]:
            if i != s and i != e:
                answer += 1
                break
            elif i == s:
                s += 1
            else :
                e -= 1
        elif tmp < A[i]:
            s += 1
        elif tmp > A[i]:
            e -= 1

print(answer)
