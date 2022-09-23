import math

def check_prime(n):
    for i in range(2, int(math.sqrt(n))+1) :
        if n % i == 0 :
            return 0
    return 1

def solution(n, k):
    answer = 0
    nnum = ''

    # k진법
    while n:
        nnum += str(n % k)
        n = n // k
    
    # 0으로 split
    tnum = nnum[::-1].split('0')
    for t in tnum:
        if t == '' : continue
        if int(t) <= 1 : continue
        answer += check_prime(int(t))

    return answer
