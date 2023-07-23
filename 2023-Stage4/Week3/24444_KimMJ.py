import sys
input = sys.stdin.readline

def BFS(v):
    global count
    q = [R]
    visited[R] = 1
    while q:
        v = q.pop(0)
        node[v].sort()
        for i in node[v]:
            # 방문 처리
            if visited[i] == 0:
                q.append(i)
                count += 1
                visited[i] = count
                
N, M, R = map(int, input().split())
node = [[] for _ in range(N+1)]

# 노드 간 연결
for _ in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
    
visited = [0] * (N+1)
count = 1

BFS(R)
for i in range(1, N+1):
    print(visited[i])
