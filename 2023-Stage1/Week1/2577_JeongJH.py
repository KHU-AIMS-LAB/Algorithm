import sys

# 세 개의 자연수 A, B, C 줄마다 입력
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

# 세 자연수의 곱 A, B, C에 대해 string으로 변환한 값을 'result' 변수에 저장
result = str(A * B * C)

# result에 0부터 9까지 각각 몇 번 쓰였는지 for문을 돌면서 count 함수를 통해 계산
for i in range(10):
    print(result.count(str(i)))
    
