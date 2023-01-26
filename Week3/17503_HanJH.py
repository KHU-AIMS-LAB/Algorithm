import sys 
from heapq import heappop, heappush

info = sys.stdin.readline().strip()

n, m, k = map(int, info.split()) # 마실수 있는 맥주의 개수, 최종 선호도, 맥주의 종류
# k개에 대한 [맥주의 선호도, 맥주 도수]를 리스트에 저장 
beers = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(k)]
beers2 = sorted(beers, key=lambda x : (x[1], x[0]))
# print(beers2) # 먼저 x[1](도수)부터 정렬이 되고(오름차순), 같은 값을 가진 것들 중에서 x[0](선호도)이 오름차순으로 정렬된다. 
# 도수부터 정렬을 해야, 선호도의 총 합을 증가시켜 가면서, 가장 낮은 간 용량을 찾을 수 있다.


heap = [] # 선호도를 저장할 heap
sum_prefer = 0  # 선호도의 합

answer = -1
# beer : (beer[0](선호도), beer[1](도수))의 형태
# 도수가 작은 것부터 시작된다. 그리고 같은 도수 중에서는 선호도가 낮은 것부터 시작된다. 
for beer in beers2:
    sum_prefer += beer[0] # 선호도를 더해준다. 
    heappush(heap, beer[0]) # 선호도를 오름차순으로 넣는다. 
    if len(heap) == n: # heap에 들어간 선호도의 개수가 n개가 되면
        if sum_prefer >= m: # 만약 최종 선호도보다 크다면 
            answer = beer[1] # 마지막으로 넣는 값의 도수가 될 것이다. -> 도수로 먼저 정렬을 했다. 그 이후에 선호도를 정렬
            # 따라서 가장 마지막에 넣어주는 값의 도수는 앞의 도수들보다 같거나 크다. 
            # 그리고 answer가 처음으로 바뀌는 순간이 가장 적은 간 용량으로 선호도를 채울수 있는 경우이므로, 그 순간 for문을 나온다. 
            break 
        else:
            sum_prefer -= heappop(heap) #만약 n개를 넣었는데, 최종 선호도보다 크지 않다면, heap에서 가장 
            # 작은 선호도를 가진 값을 선호도들의 합에서 빼주고, heap에서도 빼준다. 
            
            
if answer == -1: # 어떠한 경우에도 최종 선호도를 넘을 수 없는 경우 
    print(-1)
    exit()
        
print(answer)

# ref : https://devlibrary00108.tistory.com/271
