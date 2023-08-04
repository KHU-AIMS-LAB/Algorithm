D, K = list(map(int, input().split()))
# 1a + 0b, 0a + 1b, 1a + 1b, 1a + 2b, 2a + 3b, 3a + 5b, 5a + 8 b...의 패턴을 가진다.
# 위의 패턴에 맞춰, a / b에 대해 새로운 피보나치를 만든다.
A = [0 for _ in range(30)]
B = [0 for _ in range(30)]

A[0] = 1
B[1] = 1

breaked = False

for i in range(2, D):
    A[i] = A[i-1] + A[i-2]
    B[i] = B[i-1] + B[i-2]

# 할머니가 호랑이를 처음 만난 날에 준 떡의 개수 A, 
# 그리고 그 다음 날에 호랑이에게 준 떡의 개수 B를 찾기 위한 for문
# A[D-1] * i + B[D-1] * j == K 일 때의 i, j를 찾는다.
for i in range(1, K):
    for j in range(i, K):
        if A[D-1] * i + B[D-1] * j == K:
            print(i)
            print(j)
            breaked = True
            break
    
    if breaked == True:
        break