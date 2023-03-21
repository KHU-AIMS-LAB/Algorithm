import sys
from collections import Counter

num = int(sys.stdin.readline())
# num만큼 입력 받아 list에 저장
num_list = [int(sys.stdin.readline().strip()) for i in range(num)]

# 정렬; 입력 순서 바뀌어도 통계값에 변화X ⇒ sort()로 리스트 대체
num_list.sort()
length = len(num_list)

# 산술평균; 소수점 이하 첫째 자리에서 반올림
avg = round(sum(num_list) / length)

# 중앙값
median = num_list[length // 2]

# 최빈값; 여러 개 있을 때는 최빈값 중 두 번째로 작은 값 출력
# 입력값이 1개일 경우 오류 발생 가능 → try-except 문으로 예외 처리
# Counter(num_list): num_list 내 각 요소에 대한 개수를 dictionary 형태로 return
# most_common(): 위의 dictionary를 tuple 형태로 return
# most_common()에 argument를 통해 상위 n개의 최빈값을 return할 수 있음
common = Counter(num_list).most_common()

try:
    if common[0][1] == common[1][1]: # 최빈값이 2개 이상인 경우
        mode = common[1][0] 
    else:
        mode = common[0][0]
        
except:
    mode = common[0][0]

# 범위; 최대 - 최소
rg = max(num_list) - min(num_list)

print(f'{avg}\n{median}\n{mode}\n{rg}')
