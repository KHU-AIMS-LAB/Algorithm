import sys
from collections import deque


info = sys.stdin.readline().strip().split()
N = int(info[0])# 정점의 개수
M = int(info[1])# 간선의 개수
start = int(info[2]) # 탐색을 시작할 정점의 번호

# graph는 대부분 1번 노드부터 시작하므로, 0번째 인덱스를 만들어두고, 1번부터 시작
visited = [False] * (N+1)
graph = [[] for i in range(N+1)]

for i in range(M):
	edge = sys.stdin.readline().strip().split()
	graph[int(edge[0])].append(int(edge[1]))
	graph[int(edge[1])].append(int(edge[0]))

# print(graph)
for i in range(len(graph)):
	graph[i].sort()

# print(graph)
def dfs(graph, v, visited):
	# 현재 노드를 방문 처리
	visited[v] = True
	print(v, end = ' ' )
	# 현재 노드와 연결된 다른 노드를 재귀적으로 방문
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)
# dfs
dfs(graph, start, visited)
print()

# BFS Method 정의
def bfs(graph, start, visited):
	# Queue 구현을 위해 deque 라이브러리 사용
	queue = deque([start])
	# 현재 노드를 방문 처리
	visited[start] = True
	# 큐가 빌때까지 반복
	while queue:
		# 큐에서 하나의 원소를 뽑아 출력하기
		v = queue.popleft()
		print(v, end = ' ')
		# 아직 방문하지 않은 인접한 원소들을 큐에 삽입
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True
# 방문 여부 초기화
visited = [False] * (N+1)
bfs(graph, start, visited)
