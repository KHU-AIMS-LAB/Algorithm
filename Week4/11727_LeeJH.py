import sys

n = int(sys.stdin.readline())

dp = [1, 3, 5, 11]

# DP를 위한 점화식 : (i-2)항 * 2 + (i-1)항 이 성립
if n > 4:
    for i in range(4, n):
        dp.append((dp[i-2]) * 2 + dp[i-1])

print(dp[n-1] % 10007)