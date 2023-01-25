import sys

n = int(sys.stdin.readline())

stair = []
dp = []

for _ in range(n):
    a = int(sys.stdin.readline())
    stair.append(a)

# n이 자연수이므로 1,2,3 일 경우 예외처리
if n == 1:
    print(stair[0])
    exit()
elif n == 2:
    print(stair[0] + stair[1])
    exit()
elif n==3:
    print(max(stair[0] + stair[2], stair[1] + stair[2]))
    exit()
else:
    dp.append(stair[0])
    dp.append(stair[0] + stair[1])
    dp.append(max(stair[0] + stair[2], stair[1] + stair[2]))

# 직전 계단을 밟은 경우 -> 두개 연속을 밟을 가능성이 존재
# i - 2의 경우 -> 마지막 직전 계단을 밟으면 조건에 부합하지 않을 수 있음
# i - 3의 경우 -> 마지막 계단과 직전계단을 연속해서 밟아도 됨, (i-2 의 계단을 스킵)
for i in range(3, n):
    dp.append(max(dp[i - 2] + stair[i],  dp[i-3] + stair[i] + stair[i-1]))

print(dp[n-1])