# 3개의 int 값을 입력 받음
A = int(input())
B = int(input())
C = int(input())

# 세 값을 곱하고 string 으로 변환
target = str(A * B * C)

# 0-9 숫자를 counting 해줄 리스트를 만들어줌
idx = [0] * 10

# string 값을 순회하며 각 숫자에 해당하는 idx list를 1씩 업데이트
for i in target:
    idx[int(i)] += 1

# idx list 를 순회하며 출력
for j in idx:
    print(int(j))
