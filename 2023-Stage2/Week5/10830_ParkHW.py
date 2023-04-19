# 분할정복으로 이 문제를 해결할 수 있다!

NB = input().split()
N, B = int(NB[0]), int(NB[1])
A = []

# 제곱해야할 행렬 A를 입력 받는다
for i in range(0, N):
    A.append(list(map(int, input().split())))

# 두 행렬을 곱할 때 사용하는 함수
def mul(A, B):
    N = len(A)
    c = [[0] * N for _ in range(N)]
    # 행 순회
    for i in range(N):
        # 열 순회
        for j in range(N):
            e = 0
            # 두 행렬을 서로 곱한다
            for k in range(N):
                e += A[i][k] * B[k][j]
            # 각 요소에 대해 1000을 나눈 다음 나머지 반환
            c[i][j] = e % 1000
    return c

# 분할정복을 위해 사용하는 함수
def power(A, N):
    # N == 1 일 때는 행렬의 요소를 1000으로 나눈 다음 나머지를 반환한다
    if N == 1:
        for i in range(len(A)):
            for j in range(len(A)):
                A[i][j] %= 1000
        return A
    
    # N > 1 일 때는, 분할 정복을 통해 큰 문제를 작은 문제로 쪼갠 다음 계산할 수 있다
    # 예를 들어 4 제곱은 2제곱 * 2제곱
    # 3제곱은 2 제곱 * 1 제곱으로 문제를 분할 할 수 있다
    a = power(A, N // 2)

    if N % 2 == 0:
        return mul(a , a)
    
    else:
        return mul(mul(a, a), A)
    
result = power(A, B)
for i in result:
    print(*i, sep=" ")
