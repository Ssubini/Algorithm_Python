N, B = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

def mul(m1, m2):
    mulmatrix = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp = 0
            for k in range(N):
                tmp += m1[i][k] * m2[k][j]
            mulmatrix[i][j] = tmp % 1000
    return mulmatrix

def makeB(A,B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A

    elif B % 2 == 0:
        tmp = makeB(A, B//2)
        mulmat = mul(tmp,tmp)
        return mulmat

    elif B % 2 == 1:
        tmp = makeB(A,B-1)
        mulmat = mul(tmp,A)
        return mulmat

answer = makeB(A,B)
for i in range(N):
    print(*answer[i])