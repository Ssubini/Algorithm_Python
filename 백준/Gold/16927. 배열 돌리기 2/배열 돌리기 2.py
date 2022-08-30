import copy
N,M,R = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

# ws : 가로 시작, se : 가로 끝, hs : 세로 시작, he : 세로 끝
def rotate(ws,we,hs,he):
    global A

    tmp1 = A[hs][ws]
    tmp2 = A[he][ws]
    tmp3 = A[he][we]
    tmp4 = A[hs][we]

    for i in range(we-ws):
        A[hs][ws+i] = A[hs][ws+i+1]
    for i in range(we-ws-1,-1,-1):
        A[he][ws+i+1] = A[he][ws+i]
    for i in range(he-hs-1,-1,-1):
        A[hs+i+1][ws] = A[hs+i][ws]
    for i in range(he - hs):
        A[hs+i][we] = A[hs+i+1][we]

    A[hs+1][ws] = tmp1
    A[he][ws+1] = tmp2
    A[he-1][we] = tmp3
    A[hs][we-1] = tmp4

hl = N
wl = M
ws = 0
we = M-1
hs = 0
he = N-1


while True:
    if hl == 0 or wl == 0 : break
    cr = R % ((hl-1)*2 + (wl-1)*2)
    for i in range(cr):
        rotate(ws,we,hs,he)

    hl -= 2
    wl -= 2
    ws += 1
    we -= 1
    hs += 1
    he -= 1

for i in range(N):
    print(*A[i])


