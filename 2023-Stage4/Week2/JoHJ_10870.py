#!/usr/bin/env python
# coding: utf-8

# In[5]:



n = int(input())

n0=0
n1=1
sums = 0

def fivo(n, sums):
    
    if n == 0:
        return 0
    
    if n == 1 or n==2:
        return 1
    
    sums = fivo(n-1, sums) + fivo(n-2,sums)
    
    return sums
    
print(fivo(n, sums))

