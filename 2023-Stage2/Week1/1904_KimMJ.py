# 수 입력
n = int(input())

# 피보나치 list 초기화
fibonacci = [1, 2]

# n번째 피보나치 값 구한 후 list에 append
for i in range(2, n):
    fibonacci.append((fibonacci[i-1] + fibonacci[i-2]) % 15746)

# 값 출력    
print(fibonacci[n-1])