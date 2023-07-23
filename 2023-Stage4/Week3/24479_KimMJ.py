import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def DFS(v):
    global count
    visited[v] = count
    node[v].sort()
    for i in node[v]:
        # 방문 처리
        if visited[i] == 0:
            count += 1
            DFS(i)

N, M, R = map(int, input().split())
node = [[] for _ in range(N+1)]

# 노드 간 연결
for _ in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

visited = [0] * (N+1)
count = 1

DFS(R)
for i in range(1, N+1):
    print(visited[i])
