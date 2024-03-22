N = int(input())
li = [0]*(N+1)
li[1] = 0
if N == 1 : # N == 1 인경우 0 출력 후 종료
    print(0)
elif N == 2:
    print(1)
else :
    # li 초기값 설정
    li[2] = 1
    li[3] = 1

    for i in range(4, N+1):
        tmp = []
        tmp.append([li[i-1], i-1])
        if i % 2 == 0:
            tmp.append([li[i//2], i // 2])
        if i % 3 == 0:
            tmp.append([li[i//3], i // 3])

        # 최소로 갈 수 있는 곳 구하기
        mins = tmp[0]
        for j in range(1,len(tmp)):
            if mins[0] > tmp[j][0]:
                mins = tmp[j]

        li[i] = mins[0] + 1

    print(li[-1])