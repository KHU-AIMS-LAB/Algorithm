from collections import deque

N, M, R = list(map(int, input().split()))

# 인접행렬을 저장할 변수
uv = [[] for i in range(N)]

# 대기열을 저장할 queue
que = deque([])

# 결과 (노드방문순서) 를 저장할 변수
visit = [0 for i in range(N)]
k = 1

# dfs구현
def bfs(r):
    global visit, k, uv
    
    # 방문했음을 표시
    visit[r-1] = k
    k += 1

    # 시작값을 que에 넣음
    que.append(r)

    # que가 빌 때까지 아래 코드를 반복
    while len(que) > 0:
        # que의 값을 순서대로 뽑아서 방문
        m = que.popleft()
        for i in sorted(uv[m-1]):
            if visit[i-1] == 0:
                visit[i-1] = k
                k += 1
                que.append(i)

        
# 간선을 입력받고 uv에 기록
for i in range(M):
    u, v = list(map(int, input().split()))
    uv[u-1].append(v)
    uv[v-1].append(u)

# dfs를 실행
bfs(R)

for i in range(N):
    print(visit[i])