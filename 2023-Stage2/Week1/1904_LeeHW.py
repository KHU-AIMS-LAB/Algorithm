n = int(input()) # 입력

# a(i+2) = a(i) + a(i+1) 점화식을 풀기 위해 초기값 a(1), a(2) 세팅
if n == 1:
    print(1)

elif n == 2:
    print(2)

# n이 3 이상일 경우의 점화식
else:
    a = 1 #점화식의 초기값
    b = 2
    for _ in range(3, n+1):
        result = (a + b) % 15746 # a(i) = a(i-2) + a(i-1)
        a, b = b, result

    print(result)