import sys
input = sys.stdin.readline

while True:
    try :
        x = int(input())
        n = int(input())
        lego = [int(input()) for _ in range(n)]
        lego.sort()

        l1 = -1
        l2 = -1
        for target in range(len(lego)-1,-1,-1):
            start = 0
            end = target-1
            tn = x*10000000 - lego[target]

            while start <= end:
                mid = (start + end) // 2
                if lego[mid] == tn:
                    l1 = lego[mid]
                    l2 = lego[target]
                    break
                elif lego[mid] > tn:
                    end = mid - 1
                else :
                    start = mid + 1

            if l1 != -1 and l2 != -1 : break


        if l1 != -1 and l2 != -1:
            print('yes '+ str(l1) + ' ' + str(l2))
        else :
            print('danger')

    except:
        break