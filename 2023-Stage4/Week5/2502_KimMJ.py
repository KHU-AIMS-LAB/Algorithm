D, K = map(int, input().split())
fibo = [1, 1]
for _ in range(D-3):
    fibo.append(fibo[-1] + fibo[-2])
    
for i in range(1, K // fibo[-2] + 1):
    n = K - i * fibo[-2]
    if n % fibo[-1] == 0:
        B = n // fibo[-1]
        print(i)
        print(B)
        break