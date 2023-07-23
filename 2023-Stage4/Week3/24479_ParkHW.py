import sys
sys.setrecursionlimit(150000)

N, M, R = list(map(int, input().split()))

# 인접행렬을 저장할 변수
uv = [[] for i in range(N)]


# 결과 (노드방문순서) 를 저장할 변수
visit = [0 for i in range(N)]
k = 1

# dfs구현
def dfs(r):
    global visit, k, uv
    

    # 방문했음을 표시
    visit[r-1] = k
    k += 1

    # r에 연결된 노드를 오름차순으로 방문
    for i in sorted(uv[r-1]):
        if visit[i-1] == 0:
            dfs(i)
        
# 간선을 입력받고 uv에 기록
for i in range(M):
    u, v = list(map(int, input().split()))
    uv[u-1].append(v)
    uv[v-1].append(u)

# dfs를 실행
dfs(R)

for i in range(N):
    print(visit[i])