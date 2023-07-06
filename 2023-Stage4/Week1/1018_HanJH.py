import sys 

# M, N 입력 
M, N = map(int, input().split())

# 보드판 입력 
board = []
for i in range(M):
    row = input().replace('B', '1').replace('W', '0')
    board.append(row)


min_change_num = M * N 
for x in range(M-7):
    
    for y in range(N-7):
        
        change_num = 0
        for i in range(8):
            for j in range(8):
                if (i + j)% 2 == 0: # 흰색이어야 하는 자리 
                    if board[x+i][y+j] != '0' : # 실제 색은 검은색이라면 
                        change_num += 1
                        
                else:               # 검은색이어야 하는 자리 
                    if board[x+i][y+j] != '1': # 실제 색은 흰색이라면 
                        change_num += 1
                        
        if min_change_num > change_num :
            min_change_num = change_num
        if min_change_num > 64 - change_num:
            min_change_num = 64 - change_num

print(min_change_num) 

# 틀릴때마다 1씩 더한다. 
# 체스판이 2개가 있는데, 다른 타입의 경우는 64에서 해당 값을 빼주면 된다. 
