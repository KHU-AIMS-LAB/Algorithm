S, a, b, c = map(int, input().split())
dp = [[[[-1 for _ in range(51)] for _ in range(51)] for _ in range(51)] for _ in range(51)]

def recursion(S, a, b, c):
    case = 0
    # 남은 곡이 0인 경우
    if S == 0:
        if a == 0 and b == 0 and c == 0:
            return 1
        else:
            return 0
    
    # 부를 곡이 0인 경우
    if a < 0 or b < 0 or c < 0:
        return 0

    if dp[S][a][b][c] >= 0 :
        return dp[S][a][b][c]
    
    for i in range(2) :
        for j in range(2) :
            for k in range(2) :
                if (i == 0 and j == 0 and k == 0) :
                    continue
                case += recursion(S - 1, a - i, b - j, c - k)

    dp[S][a][b][c] = case
    return case % 1000000007


case = recursion(S, a, b, c)
print(case)