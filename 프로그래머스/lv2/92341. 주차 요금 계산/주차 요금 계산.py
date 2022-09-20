import math
from collections import defaultdict

def solution(fees, records):
    answer = []

    dict = {}
    total = defaultdict(int)
    
    for record in records :
        time, number, state = record.split()
        hour, minutes = time.split(":")
        time = int(hour) * 60 + int(minutes)
        if number in dict : # 이미 입차되어 있다면
            total[number] += time - dict[number]
            del dict[number]
        else : # 입차할 경우
            dict[number] = time

    # 출차x
    max_time = (23 * 60) + 59
    for num, t in dict.items():
        total[num] += max_time - t

    # 요금 계산
    for num, t in total.items() :
        cost = fees[1]
        if t > fees[0] : 
            cost += math.ceil((t - fees[0]) / fees[2]) * fees[3]
        answer.append([num, cost])

    # 차량 번호 오름차순
    answer.sort()
    return [a[1] for a in answer]