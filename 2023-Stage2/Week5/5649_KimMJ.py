N = int(input())
pt = []
for i in range(N):
    pt.append(list(map(int, input().split())))

# Ax = B -> x = A^-1B로 계산    
x1_square = sum(x[0]**2 for x in pt)
x1_sum = sum(x[0] for x in pt)
x1_mul_y1 = sum(x[0]*x[1] for x in pt)
y1_sum = sum(x[1] for x in pt)

det_a = 1/(x1_square * N - x1_sum ** 2) * N
det_b = 1/(x1_square * N - x1_sum ** 2) * (-x1_sum)
det_d = 1/(x1_square * N - x1_sum ** 2) * x1_square

a = round(det_a * x1_mul_y1 + det_b * y1_sum, 3)
b = round(det_b * x1_mul_y1 + det_d * y1_sum, 3)

print("%0.3f"%a)
print("%0.3f"%b)