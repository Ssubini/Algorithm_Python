import sys
import copy
input = sys.stdin.readline

N,M,x,y,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
move = list(map(int,input().split()))
dice = [0]*6

def east():
    global dice
    tmpdice = copy.deepcopy(dice)
    dice[1] = tmpdice[5]
    dice[2] = tmpdice[1]
    dice[3] = tmpdice[2]
    dice[5] = tmpdice[3]

def west():
    global dice
    tmpdice = copy.deepcopy(dice)
    dice[1] = tmpdice[2]
    dice[2] = tmpdice[3]
    dice[3] = tmpdice[5]
    dice[5] = tmpdice[1]

def north():
    global dice
    tmpdice = copy.deepcopy(dice)
    dice[0] = tmpdice[2]
    dice[2] = tmpdice[4]
    dice[4] = tmpdice[5]
    dice[5] = tmpdice[0]

def south():
    global dice
    tmpdice = copy.deepcopy(dice)
    dice[0] = tmpdice[5]
    dice[2] = tmpdice[0]
    dice[4] = tmpdice[2]
    dice[5] = tmpdice[4]

def checkEast():
    global y
    if y >= M-1 : return False
    else :
        y += 1
        return True

def checkWest():
    global y
    if y <= 0 : return False
    else:
        y -= 1
        return True

def checkNorth():
    global x
    if x <= 0 : return False
    else:
        x -= 1
        return True

def checkSouth():
    global x
    if x >= N-1 : return False
    else:
        x += 1
        return True

for k in move:
    if k == 1 :
        if checkEast() :
            east()
        else: continue
    elif k == 2 :
        if checkWest() :
            west()
        else: continue
    elif k == 3 :
        if checkNorth():
            north()
        else: continue
    elif k == 4 :
        if checkSouth():
            south()
        else: continue

    if board[x][y] == 0 :
        board[x][y] = dice[5]
    else :
        dice[5] = board[x][y]
        board[x][y] = 0

    print(dice[2])

