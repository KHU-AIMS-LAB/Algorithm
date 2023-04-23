import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]


# 행렬 곱하는 코드 
def mul(U, V):
    n = len(U)
    Z = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            Z[row][col] = e % 1000 # 애초에 너무 큰 숫자가 되지 않도록 1000의 나머지 연산을 진행한다. 

    return Z

def square(A, B):
    # 만약 1이라고 한다면, 바로 그냥 나머지 연산만 수행해서 return 
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A
    # 처음에는 2의 제곱수만 되는 줄 알았는데, 2를 기준으로 나눠서 진행(짝수, 홀수)
    # 홀수가 나오는 경우에는 해당 행렬에 A만 한번 더 곱해주면 된다. 
    tmp = square(A, B//2)
    if B % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)

result = square(A, B)
for r in result:
    # 이렇게 하면 한번에 행렬을 출력하는 것이 가능 
    print(*r)
