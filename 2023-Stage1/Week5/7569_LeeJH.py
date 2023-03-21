import sys
from collections import deque

m,n,h = map(int, sys.stdin.readline().split())
graph = []
queue = deque([])

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                queue.append([i,j,k])
    graph.append(tmp)

# 방향벡터 x,y,z 축
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

# BFS
while(queue):
    x,y,z = queue.popleft()

    for i in range(6):
        ax = x + dx[i]
        ay = y + dy[i]
        az = z + dz[i]
        # 범위 확인 후 날짜 + 1
        if 0 <= ax < h and 0 <= ay < n and 0 <= az < m and graph[ax][ay][az] == 0:
            queue.append([ax, ay, az])
            graph[ax][ay][az] = graph[x][y][z] + 1

answer = 0

# 최대값 출력
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
        answer = max(answer, max(j))
print(answer - 1)