N, B = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

def mat_mul(N, A, B):
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                matrix[i][j] += A[i][k] * B[k][j]
            matrix[i][j] %= 1000
    return matrix

def calc(A, B):
    if B == 1:
        for i in range(len(A)):
            for j in range(len(A)):
                A[i][j] %= 1000
        return A
    
    temp = calc(A, B // 2)

    if B % 2 == 1:
        return mat_mul(N, mat_mul(N, temp, temp), A)
    else:
        return mat_mul(N, temp, temp)

result = calc(A, B)

for i in result:
    for j in i:
        print(j,end= ' ')
    print()