import sys
from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
n, m, k = map(int, input().split())

soil = [[5]*n for _ in range(n)]

A = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

trees = [[deque() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c, age = map(int, input().split())
    trees[r-1][c-1].append(age)

def spring_summer():
    for i in range(n):
        for j in range(n):
            dead_amount = 0
            new_trees = deque()
            for age in trees[i][j]:
                if soil[i][j] >= age:
                    soil[i][j] -= age
                    new_trees.append(age + 1)
                else:
                    dead_amount += (age // 2)
            trees[i][j] = new_trees
            soil[i][j] += dead_amount

def fall_winter():
    tmp_trees = [] # r, c
    for i in range(n):
        for j in range(n):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    for direction in range(8):
                        nx, ny = i + dx[direction], j + dy[direction]
                        if not (0 <= nx < n and 0 <= ny < n):
                            continue
                        tmp_trees.append((nx, ny))
                        
            soil[i][j] += A[i][j]

    for tree_position in tmp_trees:
        r, c = tree_position
        trees[r][c].appendleft(1)


for i in range(k):
    spring_summer()
    fall_winter()


cnt = 0

for i in range(n):
    for j in range(n):
        for k in range(len(trees[i][j])):
            cnt += 1

print(cnt)