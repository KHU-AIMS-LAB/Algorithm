N, M, V = map(int, input().split())

node = [[] for _ in range(N+1)]

# DFS
visited = (N+1) * [0]

# BFS
visited2 = (N+1) * [0]

for i in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for i in node:
    i.sort()

def DFS(V):        
    visited[V] = 1
    print(V, end = ' ')
    for i in node[V]:
        if visited[i] == 0 :
            DFS(i)

def BFS(V):
    visited2[V] = 1
    q = [V]
    while q:
        V = q.pop(0)
        print(V, end = ' ')
        for i in node[V]:
            if  visited2[i] == 0:
                q.append(i)
                visited2[i] = 1

DFS(V)
print()
BFS(V)
