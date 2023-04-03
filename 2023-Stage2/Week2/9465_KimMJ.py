T = int(input())

for i in range(T):
    n = int(input())
    dp = []
    for _ in range(2):
        dp.append(list(map(int, input().split())))

    for j in range(1, n):
        # 2개 열일 때 각 대각선 합 계산
        if j == 1 :
            dp[0][1] += dp[1][0]
            dp[1][1] += dp[0][0]
        # 나머지 경우 j-1 열과 j-2 열을 합한 값 비교 후 큰 값으로 계산
        else :
            dp[0][j] += max(dp[1][j-1], dp[1][j-2])
            dp[1][j] += max(dp[0][j-1], dp[0][j-2])

    print(max(dp[0][-1], dp[1][-1]))
