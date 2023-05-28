#!/usr/bin/env python
# coding: utf-8

# In[25]:


# N개의 물건
# 무게 W와 가치 V
# K만큼의 무게를 넣을 수 있음.
# 배낭에 넣을 수 있는 물건들의 가치의 최댓값

from itertools import combinations

N, K = map(int, input().split())
WV = []

for i in range(N):
    W, V = map(int, input().split())
    WV.append((W, V))

''' 
메모리 초과됨.. 

# 가능한 조합의 수 구하기

all_combination = []

for i in range(N):
    combination = list(combinations(WV, i+1))
    all_combination = all_combination + (combination)
    
    
# 1번째 요소는 weight, 2번째 요소는 value (가치)

max_value = 0

for i in range(len(all_combination)):
    
    weight = 0
    value = 0
    
    for j in range(len(all_combination[i])):
        weight += all_combination[i][j][0]
        value += all_combination[i][j][1]
        
    if (weight <= K) and (value >= max_value):
        max_value = value   
    
print(max_value)

'''

#동적 그래프 다시 구성
N, K = map(int, input().split())
WV = []

for i in range(N):
    W, V = map(int, input().split())
    WV.append((W, V))

# dp[i][j]: 배낭의 무게 제한이 j일 때, i번째 물건까지 고려했을 때의 최대 가치
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1): # 1부터 5까지 
    weight, value = WV[i - 1]
    for j in range(1, K + 1):
        if weight <= j:
            # i번째 물건을 선택하는 경우와 선택하지 않는 경우 중 최댓값 선택
            dp[i][j] = max(dp[i - 1][j - weight] + value, dp[i - 1][j]) # 선택하는 경우, 선택하지 않는 경우 
        else:
            # 현재 물건을 선택할 수 없는 경우 이전 상태의 최대 가치를 그대로 가져옴
            dp[i][j] = dp[i - 1][j]

print(dp[N][K])

