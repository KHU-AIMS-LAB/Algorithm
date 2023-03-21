import sys

num = int(sys.stdin.readline())
data = []
ans = []

# 덩치를 map 형태로 입력
for i in range(num):
    a, b = map(int, input().split())
    data.append((a,b))

# a,b값 모두가 클때를 기준으로 비교하여 값 갱신
for i in range(num):
    tmp = 1
    for j in range(num):
        if (data[i][0] < data[j][0]) & (data[i][1] < data[j][1]):
            tmp += 1
    ans.append(tmp)

# 결과 출력
for a in ans:
    print(a, end=" ")