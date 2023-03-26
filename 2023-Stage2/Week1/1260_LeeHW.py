from collections import deque

n, m, start_v = map(int, input().split()) #노드 개수, 엣지 개수, 젓 노드 번호
graph = [[] for _ in range(n + 1)] # 주어진 노드와 엣지에 대한 그래프

#노드와 엣지를 그래프로 저장
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

graph = [sorted(x) for x in graph] # 각 노드별로 인접 노드의 번호를 오름차순으로 정렬


def dfs(graph, v, visited): # dfs 알고리즘 구현 (재귀함수가 스택을 사용하는 성질을 이용)
    visited[v] = True # v는 방문처리
    print(v, end=' ') # 방문된 v값 출력
    for i in graph[v]:
        if not visited[i]: # 방문되지 않은 노드에 대해
            dfs(graph, i, visited) # dfs함수 재귀 호출


def bfs(graph, start, visited): # bfs 알고리즘 구현
    queue = deque() # 자료구조 큐를 사용
    queue.append(start) # 시작 노드를 큐에 저장
    visited[start] = True # 저장된 시작노드는 방문처리

    while queue: # 큐가 빌 때까지
        v = queue.popleft() # 큐에 대해 pop 연산(가장 처음에 들어온 노드 꺼냄)
        print(v, end=' ') # 큐에서 꺼낸 노드의 값 출력
        for i in graph[v]:
            if not visited[i]: # 방문되지 않은 노드에 대해
                queue.append(i) # 큐에 저장 후
                visited[i] = True # 방문 처리


visited = [False] * (n + 1) # 모든 노드가 방문되지 않았다고 세팅
dfs(graph, start_v, visited)
print('')
visited = [False] * (n + 1) # 모든 노드가 방문되지 않았다고 세팅
bfs(graph, start_v, visited)