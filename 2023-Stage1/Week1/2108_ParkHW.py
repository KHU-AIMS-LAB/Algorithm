import sys
import math

# 입력받을 수의 개수 (N)를 입력 받음
N = int(input())

# 변수 초기화
Sum = 0
idxCnt  = 0
tempMax = 0
smallMax = 0

# -4000부터 4000까지의 count 정보를 담을 list 초기화
cnt = [0] * 8001

# min, max 값 계산을 위한 초기화
min = 4000
max = -4000

for i in range(0, N):
    # element 입력 받음
    x = int(sys.stdin.readline())
    
    # 각 element 값 더해서 Sum에 총합 기록 (Mean 계산을 위함)
    Sum += x

    # 각 element 값의 빈도 수 cnt list 에 기록 (중앙값, 최빈값 값 계산을 위함)
    cnt[x+4000] += 1

    # 최소값, 최대값의 계산
    if min > x:
        min = x
    if max < x:
        max = x
    
# 평균 계산
Mean = round(Sum / N)

# 중앙값 계산
# cnt list를 순회
for i in range(0, 8001):
    # -4000 (즉, index 0)부터 체크하여 값을 카운트 하고, N의 절반에 해당하는 index가 몇인지 알아봄
    if idxCnt < math.ceil(N * 0.5):
        idxCnt += cnt[i]
        if(idxCnt >= math.ceil(N*0.5)):
            Mid = i - 4000

# 최빈값 계산

    # -4000부터 4000까지 순회하여 cnt 값이 가장 큰 index 를 출력
    # 현재까지의 순회값 중 최빈값이 같은 경우가 없었을 때는 smallMax = 0 처리
    if tempMax < cnt[i]:
        smallMax = 0
        tempMax = cnt[i]
        Max = i - 4000

    # 현재까지의 순회값 중 최빈값이 같은 경우가 없었으나,
    # 처음으로 현재의 최빈값과 같은 빈도의 수가 나왔을 때는,
    # smallMax = 1로 업데이트 하고 해당 값을 최빈값 중 두번째로 작은 수라고 간주
    elif (tempMax == cnt[i]) and (smallMax == 0):
        smallMax = 1
        tempMax = cnt[i]
        Max = i - 4000

# 범위 계산
Range = max - min

print(Mean)
print(Mid)
print(Max)
print(Range)
