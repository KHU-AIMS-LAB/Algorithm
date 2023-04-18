import sys 
from itertools import combinations

# 입력 
M_N = input()
N, M = int(M_N.split()[0]), int(M_N.split()[1])
city = []
for i in range(N):
    city.append(sys.stdin.readline().split())

# 집과 치킨 집의 리스트 생성 
house_list = []
chicken_list = []
for i in range(N):
    for j in range(N):
        if city[i][j] == '1':
            house_list.append([i, j])
        elif city[i][j] == '2':
            chicken_list.append([i, j])

result = 1000000
for chi in combinations(chicken_list, M):
    temp = 0 
    for h in house_list: 
        chi_len = 999 
        for j in range(M):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len 
    result = min(result, temp)


print(result)
