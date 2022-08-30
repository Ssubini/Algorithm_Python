M, N, L = map(int,input().split())
shotx = list(map(int,input().split()))
animal = [list(map(int,input().split())) for _ in range(N)]

shotx.sort()
animal.sort()

answer = 0

for a in animal:
    start = 0
    end = len(shotx)-1
    while start <= end:
        mid = (start+end)//2
        catch = abs(shotx[mid]-a[0]) + a[1]

        if catch <= L :
            answer += 1
            break
        else:
            if shotx[mid] < a[0]:
                start = mid+1
            else:
                end = mid - 1

print(answer)