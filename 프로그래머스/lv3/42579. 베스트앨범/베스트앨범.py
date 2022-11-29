def solution(genres, plays):
    answer = []
    genre = {}
    for i in range(len(genres)):
        if genres[i] in genre :
            genre[genres[i]].append([i,plays[i]])
        else :
            genre[genres[i]] = [[i,plays[i]]]

    countdict = {}

    for key, values in genre.items() :
        tmp = 0
        for i in range(len(values)):
            tmp += values[i][1]

        countdict[key] = tmp

    sortedGenre = sorted(countdict.items(), key = lambda x: -x[1])

    for key in sortedGenre :
        if len(genre[key[0]]) == 1 :
            answer.append(genre[key[0]][0][0])
        else:
            genre[key[0]].sort(key = lambda x : (-x[1], x[0]))
            answer.append(genre[key[0]][0][0])
            answer.append(genre[key[0]][1][0])
    return answer


solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])