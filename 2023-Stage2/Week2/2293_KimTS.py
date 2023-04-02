def combination_coins():
    n_coins, value = map(int, input().split())
    coins_list = [int(input()) for _ in range (n_coins)]

    dp = [0]*(value+1)
    dp[0] = 1

    for coin in coins_list:
        for i in range(coin, value+1):
            dp[i] += dp[i-coin]# 동전 리스트 중 하나의 동전이 선택되었을 때, 
                               # 이후 남은 금액을 구성할 수 있는 경우의 수를 추가
        
    return dp[value]  