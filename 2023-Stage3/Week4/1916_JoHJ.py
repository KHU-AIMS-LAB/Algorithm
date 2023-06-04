#!/usr/bin/env python
# coding: utf-8

# In[7]:


import sys
import heapq

input = sys.stdin.readline

N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수

# 그래프 초기화
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())  # 출발 도시와 도착 도시

# 최소 비용 계산을 위한 우선순위 큐
pq = []
heapq.heappush(pq, (0, start))  # (비용, 도시) 형태로 큐에 추가

# 최단 거리를 저장할 배열
visited = [sys.maxsize] * (N + 1)
visited[start] = 0  # 출발 도시의 비용은 0

while pq:
    cost, city = heapq.heappop(pq)

    if visited[city] < cost:
        continue

    for next_cost, next_city in graph[city]:
        new_cost = cost + next_cost

        if new_cost < visited[next_city]:
            visited[next_city] = new_cost
            heapq.heappush(pq, (new_cost, next_city))

print(visited[end])

