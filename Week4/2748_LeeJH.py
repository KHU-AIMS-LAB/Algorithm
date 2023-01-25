# 초항 초기화
f = [0, 1]
n = int(input())
# 점화식 계산
for i in range(2, n+1):
    f.append(f[i-1] + f[i-2])
print(f[n])