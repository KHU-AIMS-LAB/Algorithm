import sys

num = int(sys.stdin.readline())
data = []
ans = []

for i in range(num):
    a, b = map(int, input().split())
    data.append((a,b))

for i in range(num):
    tmp = 1
    for j in range(num):
        if (data[i][0] < data[j][0]) & (data[i][1] < data[j][1]):
            tmp += 1
    ans.append(tmp)

for a in ans:
    print(a, end=" ")