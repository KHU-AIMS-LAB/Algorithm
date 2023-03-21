n = int(input())

# score 저장하는 s와 피보나치 함수 fb
s = [0 for i in range(len(n))]
fb = [0 for i in range(len(s))]

for i in range(n):
    s[i] = int(input())
    
fb[0] = s[0]
fb[1] = s[0] + s[1]
# 첫번째 계단을 밟고 이어 두번 째 계단 or 세 번째 계단을 밟았을 때 큰 값
fb[2] = max(s[1] + s[2], s[0] + s[2])

for i in range(3, n):
    fb[i] = max(fb[i - 3] + s[i - 1] + s[i], fb[i - 2] + s[i])
    
print(fb[n - 1])
