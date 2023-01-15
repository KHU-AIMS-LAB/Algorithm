import sys
from collections import Counter

# 이전 문제까지는 input 함수들을 통해서 입력을 받았었는데, 
# 입력 받는 개수가 많아질수록 시간 초과 오류의 가능성이 높아짐. 
# 따라서 sys.stdin.readline() 함수를 통해서 입력을 받는 것이 속도적인 측면에서 단축.

# 몇개의 수를 입력 받을 것인지 정하고, 그 수들을 입력 받아 nums라는 list에 저장 
# 준혁 -> .append()함수보다, 미리 list의 개수를 지정해 놓고 
# indexing을 통해서 요소의 값만을 변화시키는 것이 빠름.
n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))

# list내의 요소들 정렬 (-> 중앙값 계산을 위해)
nums.sort()

# 
nums_s = Counter(nums).most_common()

# 평균 출력 
print(round(sum(nums) / n))

# 중앙값 출력 
print(nums[n // 2])

# 최빈값 출력 
# Counter 함수를 통해서 빈도수 기준 내림차순으로 정렬이 되고
# 동일한 빈도수를 가진 요소값들은 오름차순으로 정렬이 되어 
# (요소, 빈도수) 의 Tuple 형태의 요소를 가진 List를 반환한다. 
if len(nums_s) > 1:
    if nums_s[0][1] == nums_s[1][1]:
        print(nums_s[1][0])
    else:
        print(nums_s[0][0])
else:
    print(nums_s[0][0])

# 범위 출력
print(nums[-1] - nums[0])
