n_test = int(input()) # Test 수 입력
for test in range(n_test):
    
    n_sticker = int(input()) # 스티커 수 입력
    dp = [list(map(int, input().split())) for _ in range(n_sticker)] # 스티커 점수 입력
    
    dp[1][0] += dp[1][0]
    dp[1][1] += dp[0][0]
    
    # 각 행 별로 현재 열의 스티커를 선택할 시, 선택 가능한 스티커들의 합 중 max를 선택  
    for i in range(2, n_sticker):
        dp[0][i] += max(dp[1][i-2], dp[1][i-1])
        dp[1][i] += max(dp[0][i-2], dp[0][i-1])
        
    print(max(dp[0][n_sticker-1], dp[1][n_sticker-1]))
    
        