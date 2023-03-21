import sys
from heapq import heappush, heappop

N, M, K = map(int, sys.stdin.readline().split())

beer_list = [list(map(int, sys.stdin.readline().split())) for i in range(K)]


# 도수를 최소화하면서 선호도는 M 이상만 하면 됨
# -> 도수 기준으로 정렬 & 오름차순으로 선호도 더해가서
# 선호도 합 M 이상인 N개의 맥주를 마실 때까지 반복
# N개를 마셨을 때 조건 만족하면 그때의 최대 도수 출력
# 조건을 만족하지 않으면 선호도가 가장 낮은 거 빼고 그 다음 꺼
# 도수는 이미 정렬되어 있으므로 조건을 heap의 in, out에는 신경쓰지 않아도 됨

# x[1](도수) 기준으로 정렬, 동일한 도수이면 x[0] 기준으로 정렬
beer_list.sort(key = lambda x: (x[1], x[0]))

fav_beer = 0
fav_heap = []

# beer[0]: 선호도, beer[1]: 도수
for beer in beer_list:
    # 선호도 heap에 추가
    heappush(fav_heap, beer[0])
    fav_beer += beer[0]

    # 조건에 맞는지 확인
    if len(fav_heap) == N: # 축제가 끝남
        if fav_beer >= M:
            print(beer[1])
            break # for문 끝
        else: # 선호도 만족 X
            fav_beer -= heappop(fav_heap)

if fav_beer < M:
    print(-1)
