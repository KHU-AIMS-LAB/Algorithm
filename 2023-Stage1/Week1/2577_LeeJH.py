# input 받기
a = int(input())
b = int(input())
c = int(input())

# string 으로 변환
s_abc = str(a * b * c)

# 정답 벡터 초기화
blank = [0,0,0,0,0,0,0,0,0,0]

# 각 값별 정답벡터에 값 추가 및 결과 출력
for i in s_abc:
    blank[int(i)] += 1
for i in range(10):
    print(blank[i])