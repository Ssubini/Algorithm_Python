def solution(s):
    nums = s.split()
    nnums = []
    for n in nums:
        nnums.append(int(n))
    nnums.sort()
    answer = str(nnums[0]) + ' ' + str(nnums[-1])
    
    return answer
