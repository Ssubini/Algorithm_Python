v, e = map(int, input().split())
edges = []
distance = [21e8] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))


def bellman_ford(start):
    distance[start] = 0
    for i in range(v):
        for j in range(e):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            if distance[cur_node] != 21e8 and distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                if i == v - 1:
                    return True

    return False

negative_cycle = bellman_ford(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, v + 1):
        if distance[i] == 21e8:
            print("-1")
        else:
            print(distance[i])