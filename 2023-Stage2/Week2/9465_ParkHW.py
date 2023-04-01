# 테스트 케이스(T)를 입력 받음
T = int(input())

for i in range(0, T):
    # 열의 개수(n)를 입력 받음
    n = int(input())
    
    # 스티커의 점수를 저장할 list 생성
    dp = []

    for j in range(0, 2):
        # 두 열의 점수 입력 받음
        dp.append(list(map(int, input().split())))

    # 각 열(n)에 대해 순회하며, 얻을 수 있는 최댓값으로 업데이트
    for k in range(1, n):
        if k == 1:
            # 1열에서는 0열에서의 대각선 값을 합하여 저장
            dp[0][k] += dp[1][k-1]
            dp[1][k] += dp[0][k-1]
        else:
            # 2열부터는 대각선 k-1열 값과 k-2열 값을 비교하여 더 큰 값을 더해줌
            dp[0][k] += max(dp[1][k-1], dp[1][k-2])
            dp[1][k] += max(dp[0][k-1], dp[0][k-2])

    # 마지막 열의 두 값 중 더 큰 값 반환
    result = max(dp[0][n-1], dp[1][n-1])
    print(result)