#!/usr/bin/env python
# coding: utf-8

# In[4]:


N = int(input())
A = []
s = 0

for i in range(N):
    A.append((int(input()), s))
    s += 1

sort_A = sorted(A)

result = []

for i in range(N):
    result.append(sort_A[i][1] - A[i][1]+1)

print(max(result))

