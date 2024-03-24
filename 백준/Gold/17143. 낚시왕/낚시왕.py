import copy

R, C, M = map(int, input().split())
board = [[[0, 0, 0] for _ in range(C + 1)] for _ in range(R + 1)]

for m in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r][c][0] = s
    board[r][c][1] = d
    board[r][c][2] = z

cshark = 0  # 잡은 상어
fman = 0


def catch():
    global cshark, fman, board

    for i in range(1, R + 1):
        if board[i][fman][2] != 0:
            cshark += board[i][fman][2]
            board[i][fman][0] = 0
            board[i][fman][1] = 0
            board[i][fman][2] = 0
            break


def moveUp(y, x, s):  # y,x 속력, 방향, 크기
    if y == 1:  # y가 1인 경우 0이 되면 범위를 벗어나기 때문에 예외
        moveDown(y, x, s)

    while s:
        if y == 1:
            return moveDown(y, x, s)

        s -= 1
        y -= 1
    return [y, x, 1]


def moveDown(y, x, s):
    if y == R:
        moveUp(y, x, s)

    while s:
        if y == R:
            return moveUp(y, x, s)

        s -= 1
        y += 1

    return [y, x, 2]


def moveLeft(y, x, s):
    if x == 1:
        return moveRight(y, x, s)

    while s:
        if x == 1:
            return moveRight(y, x, s)
        s -= 1
        x -= 1

    return [y, x, 4]


def moveRight(y, x, s):
    if x == C:
        return moveLeft(y, x, s)

    while s:
        if x == C:
            return moveLeft(y, x, s)
        s -= 1
        x += 1

    return [y, x, 3]  # y,x,방향


def moveShark():
    global board
    nboard = [[[0, 0, 0] for _ in range(C + 1)] for _ in range(R + 1)]  # 속력,이동방향,크기

    for i in range(R + 1):
        for j in range(C + 1):
            if board[i][j][2] == 0:
                continue
            else:

                if board[i][j][1] == 1:
                    ps = moveUp(i, j, board[i][j][0])  # y,x, 방향
                elif board[i][j][1] == 2:
                    ps = moveDown(i, j, board[i][j][0])
                elif board[i][j][1] == 3:
                    ps = moveRight(i, j, board[i][j][0])  # y,x,방향
                elif board[i][j][1] == 4:
                    ps = moveLeft(i, j, board[i][j][0])

                if nboard[ps[0]][ps[1]][2] == 0:  #
                    nboard[ps[0]][ps[1]][0] = board[i][j][0]
                    nboard[ps[0]][ps[1]][1] = ps[2]
                    nboard[ps[0]][ps[1]][2] = board[i][j][2]
                elif nboard[ps[0]][ps[1]][2] < board[i][j][2]:
                    nboard[ps[0]][ps[1]][0] = board[i][j][0]
                    nboard[ps[0]][ps[1]][1] = ps[2]
                    nboard[ps[0]][ps[1]][2] = board[i][j][2]

    board = copy.deepcopy(nboard)


while fman < C:
    fman += 1
    catch()
    moveShark()

print(cshark)