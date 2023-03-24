# 집 개수 입력 받음
N = int(input())

# 각 집에 대해 순회
for i in range(0, N):
    # R, G, B cost 를 입력 받음
    cmd = input().split()
    R, G, B = int(cmd[0]), int(cmd[1]), int(cmd[2])

    if i == 0:
        # 첫번째 집에 대해서는 R, G, B 각각을 선택했을 때의 최소 cost를 R, G, B 그 자체로 둘 수 있음
        R_temp, G_temp, B_temp = R, G, B
    else:
        # 두번째 집 부터는, 두번째집을 R/G/B 각각으로 선택했을 때의 경우의 수를 모두 고려하여
        # 각각의 최소비용을 기록해두고, 다음 집으로 값을 넘김
        R_dp = min(G_temp, B_temp) + R
        G_dp = min(R_temp, B_temp) + G
        B_dp = min(R_temp, G_temp) + B

        R_temp, G_temp, B_temp = R_dp, G_dp, B_dp

# 마지막 집의 최소비용의 최소값을 반환
result = min(R_temp, G_temp, B_temp)
print(result)