N, max_W = map(int, input().split())
knap = []
for _ in range(N):
    knap.append(list(map(int, input().split())))
    
def knapsack(N, knap, W):
    P = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        # weight 비교 후 value 업데이트
        for j in range(W + 1):
            if i==0 or j==0:
                P[i][j] = 0
            elif knap[i-1][0] <= j :
                P[i][j] = max(P[i-1][j], knap[i-1][1]+P[i-1][j-knap[i-1][0]])
            else:
                P[i][j] = P[i-1][j]
    return P

result = knapsack(N, knap, max_W)
print(result[-1][-1])