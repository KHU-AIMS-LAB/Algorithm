import sys
from queue import PriorityQueue

input = sys.stdin.readline

N = int(input())
M = int(input())

# 노선, cost 저장
route = [[] for _ in range(N + 1)]
max_cost = 1
for _ in range(M):
    dep, dst, cost = map(int, input().split())
    route[dep].append((dst, cost))
    max_cost += cost
dep, dst = map(int, input().split())


visited = [0] * (N+1)
dist = [max_cost] * (N+1)
queue = PriorityQueue()
queue.put((0,dep))
dist[dep] = 0

# priority queue로 cost 비교
def dijkstra():
    while not queue.empty():
        node = queue.get()[1]
        if visited[node]:
            continue
        visited[node] = True
        for i in route[node]:
            distance = dist[node] + i[1]
            if dist[i[0]] > distance:
                dist[i[0]] = distance
                queue.put((distance , i[0]))
dijkstra()
print(dist[dst])