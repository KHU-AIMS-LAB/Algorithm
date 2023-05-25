"""import sys 
from itertools import combinations

N = int(input())


matrix = []
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().strip().split())))

# min_diff 초기화 
min_diff = 100 * N**2

sub_num = range(1, N+1)
start_team_list = combinations(sub_num, N//2)
# track_team = list(set(sub_num).difference(set(start_team)))

for start_team in start_team_list:
    # 한쌍의 start_team과 track_team이 정해진다. 
    start_team = list(start_team)
    track_team = list(set(sub_num).difference(set(start_team)))

    # score(두팀의 점수 차이) 초기화 
    score = 0

    # start team의 점수를 계산 
    for idx_1 in range(len(start_team)):
        for idx_2 in range(idx_1+1, len(start_team)):
            # start_team은 score를 더하고, track_team은 score를 뺀다. 
            score += matrix[start_team[idx_1] - 1][start_team[idx_2] - 1]
            score += matrix[start_team[idx_2] - 1][start_team[idx_1] - 1]
            score -= matrix[track_team[idx_1] - 1][track_team[idx_2] - 1]
            score -= matrix[track_team[idx_2] - 1][track_team[idx_1] - 1]

    # 점수를 
    score = abs(score)
    # 만약 score의 차이가 지금까지의 score 차이보다 작다면, 갱신 
    if score < min_diff: 
        min_diff = score

print(min_diff)
    


    """

def dfs(depth, idx):
    global min_diff
    # 만약 depth가 n//2가 채워졌다면, 즉, start_team의 인원이 n//2명이라면 
    if depth == n//2:
        # start team과 track team의 점수 
        power1, power2 = 0, 0 
        for i in range(n):
            for j in range(n):
                # start team
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                # track team 
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]

        min_diff = min(min_diff, abs(power1 - power2))
        return 
    
    # 아니라면, 즉, 아직 start team의 인원이 덜 채워졌다면, 
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True 
            dfs(depth+1, i+1)
            visited[i] = False


n = int(input())

visited = [False for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)

dfs(0,0)
print(min_diff)
