#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys

N, L, R = map(int, sys.stdin.readline().rstrip().split())
NARA = []
OPEN = [[0] * N for _ in range(N)] 
for _ in range(N):
    NARA.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 연합 형성
def create_union():
    global NARA, OPEN
    # 방문 여부를 확인하기 위한 visited 배열
    visited = [[0] * N for _ in range(N)]
    # 상하좌우 이동을 위한 dx, dy 배열
    dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dy = [0, 0, -1, 1]
    # 연합 그룹을 나타내는 group
    group = 1
    # 인구 이동이 발생하는지 확인하는 변수
    is_move = False
    
    for i in range(N):
        for j in range(N):
            # 아직 방문하지 않은 나라인 경우
            
            if visited[i][j] == 0:
                
                visited[i][j] = group  # 그룹 번호로 방문 표시
                total_pop = NARA[i][j]  # 연합의 총 인구 수
                total_nations = 1  # 연합을 이루고 있는 나라의 개수
                queue = [(i, j)]  # BFS를 위한 큐
                
                # BFS를 통해 연합 그룹 형성
                while queue:
                    x, y = queue.pop(0)
                    # 상하좌우 인접한 나라들을 확인
                    
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        
                        # 범위를 벗어나는 경우
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue
                            
                        # 이미 방문한 나라인 경우
                        if visited[nx][ny] != 0:
                            continue
                            
                        # 국경선이 열리는 조건을 만족하는 경우
                        if L <= abs(NARA[x][y] - NARA[nx][ny]) <= R:
                            visited[nx][ny] = group  # 그룹 번호로 방문 표시
                            total_pop += NARA[nx][ny]
                            total_nations += 1
                            queue.append((nx, ny))
                            is_move = True  # 인구 이동이 발생하였음을 표시
                
                # 연합의 인구 이동 처리
                if is_move:
                    avg_pop = total_pop // total_nations
                    
                    for i in range(N):
                        for j in range(N):
                            
                            if visited[i][j] == group:
                                NARA[i][j] = avg_pop
                                
                    group += 1
                else:
                    group += 1
    return is_move

# 인구 이동이 며칠 동안 발생하는지 계산
days = 0
while True:
    if not create_union():
        break
    days += 1

print(days)

