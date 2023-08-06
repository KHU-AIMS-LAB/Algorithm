from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

dir_x = [0, 0, 1, -1]
dir_y = [1, -1, 0, 0]


result = 0
temp = [[0] * M for _ in range(N)]

#바이러스 전파
def virus(temp, x, y):  
    for i in range(4):
        nx = x+dir_x[i]
        ny = y+dir_y[i]
        if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
            temp[nx][ny] = 2
            virus(temp, nx, ny)


def count(temp):
    safe_area = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                safe_area += 1
    return safe_area



# 빈칸 좌표 구하기
blank_idx = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            blank_idx.append((i, j))

for coordinates in list(combinations(blank_idx, 3)):
    # 빈칸에 벽 설치
    for coordinate in coordinates:
        x, y = coordinate
        lab[x][y] = 1

    # 바이러스 전파
    for i in range(N):
        for j in range(M):
            temp[i][j] = lab[i][j]

    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                virus(temp, i, j)

    result = max(result, count(temp))

    # 설치한 벽 제거
    for coordinate in coordinates:
        x, y = coordinate
        lab[x][y] = 0

print(result)