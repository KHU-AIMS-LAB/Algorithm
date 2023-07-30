from collections import deque

R, C = map(int, input().split())
forest = [list(map(str, input())) for _ in range(R)]

dir_x = [0, 0, 1, -1]
dir_y = [1, -1, 0, 0]

# 물 확장
water = [[0] * C for _ in range(R)]
q = deque()
for i in range(R):
    for j in range(C):
        # 물 위치
        if forest[i][j] == '*':
            q.append((i, j))
            water[i][j] = 0
        # 굴 위치
        elif forest[i][j] == 'D':
            cave_i, cave_j = i, j
        # 고슴도치 위치
        elif forest[i][j] == 'S':
            hedgehog_i, hedgehog_j = i, j
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dir_x[i], y + dir_y[i]
        if 0 <= nx < R and 0 <= ny < C:
            # 굴 or 바위거나 물이 아니면 확장 불가
            if forest[nx][ny] == 'D' or forest[nx][ny] == 'X' or water[nx][ny]!= 0:
                continue
            q.append((nx, ny))
            water[nx][ny] = water[x][y] + 1

# 고슴도치 이동
hedgehog = [[0] * C for _ in range(R)]
q = deque()
q.append((hedgehog_i, hedgehog_j))
hedgehog[hedgehog_i][hedgehog_j] = 0

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dir_x[i], y + dir_y[i]
        if 0 <= nx < R and 0 <= ny < C:
            # 가려는 곳이 방문한 적 있거나 돌이거나 물이라면 이동 불가
            if hedgehog[nx][ny] != 0 or forest[nx][ny] == 'X' or ((hedgehog[x][y] + 1) >= water[nx][ny] and water[nx][ny] != 0):
                continue
            q.append((nx, ny))
            hedgehog[nx][ny] = hedgehog[x][y] + 1

if hedgehog[cave_i][cave_j] == 0:
    print("KAKTUS")
else:
    print(hedgehog[cave_i][cave_j])