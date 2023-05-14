N = int(input())
value = []
max_temp = [0] * 3
min_temp = [0] * 3
max_dp = [0] * 3
min_dp = [0] * 3

for i in range(N):
    value = (list(map(int, input().split())))
    for j in range(3):
        # 왼쪽 줄
        if j == 0:
            max_dp[0] = value[0] + max(max_temp[0], max_temp[1])
            min_dp[0] = value[0] + min(min_temp[0], min_temp[1])
        # 가운데 줄
        elif j == 1:
            max_dp[1] = value[1] + max(max_temp[0], max_temp[1], max_temp[2])
            min_dp[1] = value[1] + min(min_temp[0], min_temp[1], min_temp[2])
        # 오른쪽 줄
        else:
            max_dp[2] = value[2] + max(max_temp[1], max_temp[2])
            min_dp[2] = value[2] + min(min_temp[1], min_temp[2])
    # copy로 메모리 줄이고, 최대 최소 업데이트
    max_temp = max_dp[:]
    min_temp = min_dp[:]

print(max(max_dp), min(min_dp))