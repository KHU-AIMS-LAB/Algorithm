N, M = list(map(int, input().split()))
WV = [(0, 0)]

for i in range(N):
    W, V = list(map(int, input().split()))
    WV.append((W, V))

# (물건 수 + 1) x (버틸 수 있는 무게 + 1) 크기의 dp 테이블을 생성
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

# dp row 를 순회
for i in range(1, N + 1):
    W, V = WV[i]
    # dp column 을 순회
    for j in range(1, M + 1):
        # 물건 무게가 버틸 수 있는 무게보다 작거나 같을 때
        if W <= j:
            # dp의 가치를 이전 물건까지의 최대 가치와
            # 현재 물건 가치 + 이전까지 물건 중 남은 무게에 적합한 물건의 최대 가치
            # 중 큰 값으로 업데이트 한다.
            dp[i][j] = max(dp[i -1][j], dp[i-1][j-W] + V)
        # 물건 무게가 버틸 수 있는 무게보다 크면 추가하지 못하므로,
        # 이전 물건까지의 최대 가치로 업데이트 해준다.
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])