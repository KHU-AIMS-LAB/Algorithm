from collections import deque

N, L, R = map(int,input().split())
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))

dir_x = [0, 0, 1, -1]
dir_y = [1, -1, 0, 0]
day = 0

def BFS (x, y):
    q = deque()
    q.append((x, y))    
    temp = [(x, y)] # 국경선 공유 국가 좌표
    while q:
        a, b = q.popleft()
        for i in range(4):
            temp_x = a + dir_x[i]
            temp_y = b + dir_y[i]
            if 0 <= temp_x < N and 0 <= temp_y < N and visited[temp_x][temp_y] == 0:
                if L <= abs(A[temp_x][temp_y] - A[a][b]) <= R:
                    visited[temp_x][temp_y] = 1
                    q.append((temp_x, temp_y))
                    temp.append((temp_x, temp_y))
    return temp
            
while True:
    flag = 0
    visited = [[0] * (N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                union = BFS(i,j)
	   # 국경선 open 후 인구 이동
                if len(union) > 1:
                    flag = 1
                    people = sum([A[x][y] for x, y in union]) // len(union)
                    for x, y in union:
                        A[x][y] = people
    if flag == 0:
        break
    day += 1
print(day)