import sys 



n, k = map(int, sys.stdin.readline().strip().split())

stuff = [[0,0]]
knapsack = [[0 for _ in range(k+1)] for _ in range(n + 1)]

for i in range(n):
    stuff.append(list(map(int, sys.stdin.readline().strip().split())))



for i in range(1, n + 1):
    for j in range(1, k+1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight : 
            knapsack[i][j] = knapsack[i-1][j] # weight보다 작으면 위의 값을 그대로 
        else:
            knapsack[i][j] = max(value + knapsack[i-1][j-weight], knapsack[i-1][j])


print(knapsack[n][k])

