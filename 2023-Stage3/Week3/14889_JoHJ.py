#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from itertools import combinations
# 1~N 까지 조정
# Sij는 i 번 사람과 j 번 사람이 같은 팀에 속했을 때 팀에 더해지는 능력치

N = int(input())
S = []


for i in range(N):
    S.append(list(map(int, input().split())))
    
def calculate_ability_diff(N, S):
    min_diff = float('inf') # 최소차이 저장하는 변수
    
    # 가능한 모든 팀 조합을 생성
    team_combinations = list(combinations(range(N), N//2))
    
    for comb in team_combinations:
        start_team = comb # 생성된 조합임 
        link_team = tuple(x for x in range(N) if x not in comb) #링크 조합
        
        start_ability = sum(S[i][j] for i in start_team for j in start_team if i != j)
        link_ability = sum(S[i][j] for i in link_team for j in link_team if i != j)
        
        # 능력치 차이의 최소값 갱신
        
        min_diff = min(min_diff, abs(start_ability - link_ability))

    return min_diff


print(calculate_ability_diff(N, S))

