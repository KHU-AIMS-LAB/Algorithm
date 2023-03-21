import sys

n = int(sys.stdin.readline())

# 피보나치 수열 저장하는 리스트 fb
fb = (n + 1) * [0]
fb[1] = 1

for i in range(2, n+1):
    fb[i] = fb[i-1] + fb[i-2]


print(fb[n])
