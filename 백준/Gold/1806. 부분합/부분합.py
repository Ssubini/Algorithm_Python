N, S = map(int,input().split())
board = list(map(int,input().split()))
minlen = 21e8
s = 0
e = 0
tsum = board[0]

if sum(board) < S :
    print(0)
else :
    while True:
        if s == N:
            break

        if tsum >= S :
            minlen = min(minlen, e-s+1)
            tsum -= board[s]
            s += 1
        elif tsum < S :
            if e < N-1:
                e += 1
                tsum += board[e]
            else:
                s = N

    print(minlen)