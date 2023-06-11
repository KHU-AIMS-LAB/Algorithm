N = int(input())
arr = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N)]

# 숫자 1개일 때 경우의 수
dp[0][arr[0]] = 1

# 숫자 2개 이상일 때 경우의 수
for i in range(1, N-1):
    for j in range(21):
        # plus
        if 0 <= j + arr[i] <= 20:
            dp[i][j + arr[i]] += dp[i-1][j]   
        # minus
        if 0 <= j - arr[i] <= 20:
            dp[i][j - arr[i]] += dp[i-1][j]

print(dp[-2][arr[-1]])