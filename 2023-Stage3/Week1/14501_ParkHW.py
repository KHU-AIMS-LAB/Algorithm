N = int(input())
lst = []
dp = [0 for _ in range(N+1)]

for i in range(0, N):
    TP = input().split()
    T, P = int(TP[0]), int(TP[1])
    lst.append((T, P))

# 상담 일정표 순회 (시작점 선택)
for i in range(N):
    # 시작점 + 상담일(T)부터 다시 순회
    for j in range(i+lst[i][0], N+1):
        # 이때까지 순회한 상담금액 (P) + 현재의 상담금액 (P) 계산
        # 현재까지의 dp 값과 비교하여 dp 리스트 업데이트
        if dp[j] < dp[i] + lst[i][1]:
            dp[j] = dp[i] + lst[i][1]

print(dp[-1])
    