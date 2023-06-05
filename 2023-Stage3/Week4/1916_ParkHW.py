import heapq
# 목표: A번째 도시에서 B번째 도시까지 드는 버스 비용의 최소화

N = int(input()) # 도시
M = int(input()) # 버스

INF = int(1e9)
busList = [[] for _ in range(N+1)] # A와 B사이의 거리를 나타내는 행렬
distance = [INF] * (N+1) # 출발점으로부터 최단 거리를 저장할 배열

# 버스 정보와 출발, 도착지를 입력 받음
for i in range(M):
    bus = list(map(int, input().split()))
    busList[bus[0]].append((bus[1], bus[2]))

objective = list(map(int, input().split()))

# 다익스트라 알고리즘을 통해 최단 거리 계산
def dijkstra(start):
    q = []
    # 시작노드부터 탐색
    heapq.heappush(q, (0, start))
    # start -> start의 거리를 0으로 설정
    distance[start] = 0
    
    # queue에 남아있는 노드가 없을 때까지 순회
    while q:
        # 거리를 탐색할 노드를 가져옴
        dist, v = heapq.heappop(q)
        
        # 계산해둔 start -> v 의 거리보다 현재 거리가 더 길면 패스
        if distance[v] < dist:
            continue
        
        # 현재 거리가 더 짧으면 갱신
        for i in busList[v]:
            # busList를 순회하며 해당 노드를 거쳐 갈 때의 거리를 계산
            cost = dist + i[1]
            # 거쳐갈 때의 거리가 계산해둔 거리보다 작으면 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # 다음 인접 거리 계산을 위해 queue에 삽입
                heapq.heappush(q, (cost, i[0]))

dijkstra(objective[0])
print(distance[objective[1]])
