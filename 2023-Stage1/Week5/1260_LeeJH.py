from queue import Queue

# dfs는 방문노드를 1로
def dfs(vertex):
    print(vertex, end=' ') # 현재 방문 노드
    visit[vertex] = 1 # 방문표시
    for i in range(1, n+1):
        if (visit[i] == 1) | (matrix[vertex][i] == 0): # 방문노드, vertex간의 간선이 없는 것은 스킵
            continue
        dfs(i) # 재귀호출

# bfs는 방문노드를 0으로 
def bfs(vertex):
    que = Queue()
    que.put(vertex)
    visit[vertex] = 0 # 방문표시
    while(not que.empty()):
        vertex = que.get() # 현재 방문 노드
        print(vertex, end=' ')
        for i in range(1, n+1):
            if ((visit[i] == 0) | (matrix[vertex][i] == 0)): # 방문노드, vertex간의 간선이 없는 것은 스킵
                continue
            que.put(i)
            visit[i] = 0 # 방문표시


if __name__ == "__main__":
    n, m, v = map(int, input().split())
    
    visit = [0 for _ in range(n+1)] # 방문 리스트
    matrix = [[0] * (n+1) for _ in range(n+1)] # 인접노드 리스트

    for i in range(m):
        x,y = map(int, input().split())
        matrix[x][y] = 1
        matrix[y][x] = 1

    dfs(v)
    print()
    bfs(v)
