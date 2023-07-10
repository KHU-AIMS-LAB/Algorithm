N = int(input())

# 피보나치 재귀함수
def fib(n):
    # N == 0 일 때는 0, N == 1일 때는 1 출력
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    # 0과 1 이 아닐 때는 전값과 전전 값을 더해서 RETURN
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(N))