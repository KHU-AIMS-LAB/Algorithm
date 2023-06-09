num = int(input())
nums = list(map(int, input().split()))

# 21 (행) x nums - 1(열)로 이루어진 dp를 만듦
dp = [[0] * 21 for _ in range(num-1)]
# 첫 행에는 첫 숫자에 해당하는 열에 1을 채워둠
dp[0][nums[0]] = 1


# 각 행/열을 순회하며, 
for i in range(1, num-1):
    for j in range(0, 21):
        # 전 행에서 활성화된 숫자들에 대해 
        if dp[i-1][j] != 0:
            # +, - 현재값을 진행하고, 0-20 사이에 들어가면
            if j + nums[i] <= 20:
                #  경우의 수를 더해서 현재 행의 값을 업데이트 해줌
                dp[i][j+nums[i]] += dp[i-1][j]
            if j - nums[i] >= 0:
                dp[i][j-nums[i]] += dp[i-1][j]

print(dp[num-2][nums[-1]])