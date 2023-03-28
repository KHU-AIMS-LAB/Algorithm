n = int(input())
home = []

for i in range(n):
    home.append(list(map(int, input().split())))

# RGB를 선택한 모든 경우에 대해 최솟값만이 더해져 나오기 때문에 최솟값만 선택
for i in range(1, len(home)):
    home[i][0] = min(home[i - 1][1], home[i - 1][2]) + home[i][0]
    home[i][1] = min(home[i - 1][0], home[i - 1][2]) + home[i][1]
    home[i][2] = min(home[i - 1][0], home[i - 1][1]) + home[i][2]

print(min(home[n - 1][0], home[n - 1][1], home[n - 1][2]))