def fibo(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        a = fibo(n-1) + fibo(n-2)
        return a

n = int(input())
result = fibo(n)
print(result)