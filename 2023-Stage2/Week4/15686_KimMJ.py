N, M = map(int, input().split())
house = []
chicken = []

for i in range(N) :
    city = list(map(int, input().split()))
    for j in range(N) :
        if city[j] == 1 :
            house.append((i,j))
        elif city[j] == 2 :
            chicken.append((i,j))

# 최소 거리 계산
def distance(chicken) :
    dist = 0
    for w1, h1 in house :
        dist_list = []
        for w2, h2 in chicken :
            dist_list.append(abs(w1-w2) + abs(h1-h2))
        dist += min(dist_list)
    return dist

# DFS를 이용한 남길 치킨집 선택
def DFS(L, current) :
    global m_dist
    if L == M :
        selected = []
        for i in range(len(chicken)):
            if visited[i]:
                selected.append(chicken[i])
        m_dist = min(m_dist, distance(selected))
        return
   
    for i in range(current, len(chicken)) :
        if visited[i] == 0 :
            visited[i] = 1
            DFS(L + 1, i + 1)
            visited[i] = 0
            
if len(chicken) == M :
    print(distance(chicken))
else :
    m_dist = 50 * 50 * 13
    visited = [0] * len(chicken)
    DFS(0, 0)
    print(m_dist)
