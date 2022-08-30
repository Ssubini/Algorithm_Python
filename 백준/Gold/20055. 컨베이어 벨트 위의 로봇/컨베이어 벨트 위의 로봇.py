from collections import deque
N, K = map(int,input().split())
A = deque(map(int,input().split()))
robot = deque([0]*(2*N))
count = 0

while True:
    # 종료조건
    acnt = 0
    for a in A:
        if a == 0 :
            acnt += 1

    if acnt >= K : break

    # 벨트 회전
    tmpa = A.pop()
    A.appendleft(tmpa)
    tmpr = robot.pop()
    robot.appendleft(tmpr)
    robot[N-1] = 0 # 로봇 내림

    # 로봇 이동
    for i in range(N-2,-1, -1):
        if robot[i] != 0 and robot[i+1] == 0:
            if A[i+1] >= 1:
                robot[i+1] = robot[i]
                robot[i] = 0
                A[i+1] -= 1

    robot[N-1] = 0

    # 로봇 올리기
    if A[0] != 0 :
        robot[0] = 1
        A[0] -= 1

    count += 1

print(count)
