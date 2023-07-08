#!/usr/bin/env python
# coding: utf-8

# ### 1018: MXN 크기의 보드

# In[51]:


N, M = list(map(int, input().split()))
board = list()

for i in range(N):
    m = list(input())
    board.append(m)
    
result = []

for i in range(0, N-7):
    for j in range(0, M-7):
        min_change = 64
        white = 0
        black = 0

        for idx in range(i, i+8):
            for jdx in range(j, j+8):
                if (idx + jdx) % 2 == 0:  # 체스판의 색 패턴을 유지하기 위한 조건
                    if board[idx][jdx] != 'W':  # W로 칠해져야 하는 경우
                        white += 1
                    if board[idx][jdx] != 'B':  # B로 칠해져야 하는 경우
                        black += 1
                else:
                    if board[idx][jdx] != 'B':  # B로 칠해져야 하는 경우
                        white += 1
                    if board[idx][jdx] != 'W':  # W로 칠해져야 하는 경우
                        black += 1

        result.append(white)
        result.append(black)

print(min(result))
   

