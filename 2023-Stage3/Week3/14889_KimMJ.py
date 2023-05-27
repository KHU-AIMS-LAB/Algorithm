from itertools import combinations
N  = int(input())
all_stat = []
for _ in range(N):
    all_stat.append(list(map(int, input().split())))

number = list(range(N))
min_stat = float('inf')

for start in list(combinations(number, N//2)):
    start_stat = 0
    link_stat = 0
    # 전체에서 start 제외
    link =  [x for x in number if x not in start]
    # start stat 계산
    for i, j in list(combinations(start, 2)):
        start_stat += all_stat[i][j]
        start_stat += all_stat[j][i]
    # link stat 계산
    for i, j in list(combinations(link, 2)):
        link_stat += all_stat[i][j]
        link_stat += all_stat[j][i]
    min_stat = min(min_stat, abs(start_stat - link_stat))

print(min_stat)