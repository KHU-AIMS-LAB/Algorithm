N = int(input())
A = []

# 버블 정렬을 몇 번 수행해서 정렬이 완성되는지 계산하는 문제
# elem은 A의 숫자의 순서를 기록하기 위해 존재하는 변수
elem = 0

# (숫자, 인덱스 순서)를 A에 저장
for i in range(N):
    a = int(input())
    A.append((a, elem))
    elem += 1

# A을 sorting
sortedA = sorted(A)

# 인덱스 차 중 가장 큰 값을 기록하기 위한 변수
maxElem = 0

# 각 변수의 인덱스가 정렬 전후로 얼마나 차이가 나는지 파악
# 가장 값이 큰 인덱스 차이를 기록해두고 +1를 하여 프린트
for i in range(N):
    if maxElem < sortedA[i][1] - i:
        maxElem = sortedA[i][1] - i

print(maxElem + 1)
