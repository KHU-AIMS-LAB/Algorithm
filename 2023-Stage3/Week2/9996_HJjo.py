#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 총 풀이 시간 29분 26초
# 9996 번 : 한국이 그리울 땐 서버에 접속하지
# input N 설정

N = int(input())
pattern = input()
front, end = pattern.split('*')
for _ in range(N):
    filename = input()
    if len(filename) < len(front) + len(end):
        result = 'NE'
    elif filename[:len(front)] == front and filename[-len(end):] == end:
        result = 'DA'
    else:
        result = 'NE'
    print(result)

