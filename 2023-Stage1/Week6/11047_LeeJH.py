import sys

n, k = map(int, sys.stdin.readline().split())

coin = []

for _ in range(n):
    a = int(sys.stdin.readline())
    coin.append(a)

cnt = 0

# 큰 동전부터 빼가면서 몇개의 동전이 사용되는지 계산
# 큰 동전을 사용하면 다음으로 큰 동전을 사용
for i in reversed(range(n)):
    cnt += k // coin[i]
    k = k % coin[i]

print(cnt)