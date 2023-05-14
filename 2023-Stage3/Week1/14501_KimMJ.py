N = int(input())

T, P = [], []
dp = [0] * (N+1)

for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    # i-th 날에 상담한 경우, i + 상담 기간부터 마지막까지 수익 비교
    for j in range(i + T[i], N+1):
        if dp[j] < dp[i] + P[i]:
            dp[j] = dp[i] + P[i]

print(dp[-1])
