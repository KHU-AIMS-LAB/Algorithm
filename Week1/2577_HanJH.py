# 입력 
A = int(input())
B = int(input())
C = int(input())

# 세 수의 곱을 계산 후 string으로 형변환 
total_mul = A * B * C 
total_mul = str(total_mul)


# count함수를 통해서 0 ~ 9사이의 숫자를 count 
for i in range(0, 10):
    print(total_mul.count(str(i)))
