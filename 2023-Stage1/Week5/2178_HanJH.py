from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))


# 너비 우선 탐색
def bfs(x, y):
    # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # deque 생성
    queue = deque()
    queue.append((x, y)) # 현재 위치를 넣는다.

    while queue:
        x, y = queue.popleft() # 현재 위치

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 전체 사각형 안에서 돌아다녀야 함
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 0인 곳은 벽
            if graph[nx][ny] == 0:
                continue

            # 벽이 아니므로 이동
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 마지막 값에서 카운트 값을 뽑는다.
    return graph[N - 1][M - 1]


print(bfs(0, 0))
