from collections import deque

puyo = 0
N, M = 12, 6
field = [list(input().strip()) for _ in range(N)]

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

# 같은 색으로 붙어있는 좌표 return
def bfs(x, y, color):
    location = set()
    queue = deque()
    queue.append((x, y))
    
    while queue:
        node = queue.popleft()
        if node in location:
            continue
        location.add(node)
        for i in range(4):
            nx, ny = node[0] + dx[i], node[1] + dy[i]
            if (0 <= nx < N and 0 <= ny < M) and field[nx][ny] == color:
                queue.append((nx, ny))
    return location

def down():
    for y in range(M):
        for x in range(N-1, -1, -1):
            if field[x][y] != '.':
                for k in range(N-1, x, -1):
                    if field[k][y] == '.':
                        field[k][y] = field[x][y]
                        field[x][y] = '.'

while(True):
    check = 0
    for i in range(N-1, -1, -1):
        for j in range(M):
            if field[i][j] == '.':
                continue
            # 바닥에서부터 같은 색으로 붙은 좌표들 return
            array = bfs(i, j, field[i][j])
            # 4개 이상이면 연쇄
            if len(array) >= 4:
                check = 1
                for x, y in array:
                    field[x][y] = '.'
    down()
    if check == 1 :
        puyo += 1
    else :
        break
print(puyo)