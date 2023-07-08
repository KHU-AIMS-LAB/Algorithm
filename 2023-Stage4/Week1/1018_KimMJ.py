N, M = map(int, input().split())
board = []

for i in range(N):
    board.append(list(input()))
    
# 맨 왼쪽 위 칸이 흰색인 경우
case1 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']

# 맨 왼쪽 위 칸이 검은색인 경우
case2 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']

# 최대 교체 횟수 초기화
min_ct = N * M

for i in range(N-7) :
    for j in range(M-7) :
        square8x8 = [temp[j:j+8] for temp in board[i:i+8]]
        white, black = 0, 0
        for m in range(8):
            for n in range(8):
                if (square8x8[m][n] != case1[m][n]) :
                    white += 1
                if (square8x8[m][n] != case2[m][n]) :
                    black += 1
        if min_ct > min(white, black) :
            min_ct = min(white, black)

print(min_ct)