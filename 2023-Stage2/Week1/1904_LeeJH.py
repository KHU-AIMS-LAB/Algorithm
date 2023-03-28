import sys

n = int(sys.stdin.readline())

dp = [0] * 1000001

# n이 1일때와 2일때
dp[1] = 1
dp[2] = 2

# 결국 두개가 붙어버려서 n-1일때에 1을 붙이는 경우, 
# n-2일때 00을 붙이는경우 2개를 더한것이 n번째의 정답이다.

for k in range(3,n+1):
    dp[k] = (dp[k-1]+ dp[k-2])%15746
print(dp[n])