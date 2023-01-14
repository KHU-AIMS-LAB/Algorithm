import sys
from collections import Counter

# Counter는 사전(dict) 클래스의 하위 클래스로 리스트나 
# 튜플에서 각 데이터가 등장한 횟수를 사전 형식으로 돌려준다.
# most_common() 메소드는 등장한 횟수를 
# 내림차순으로 정리하여 보여준다. 

n = int(input())

# PS에서 python의 입력 테크닉. 배열을 미리 초기화 하고
# append 대신 indexing을 이용하여 배열을 저장하는 것이 더 효율적이다.
arr = [0 for _ in range(n)]

for i in range(n):
    arr[i] = int(sys.stdin.readline())

arr.sort()

print(round(sum(arr)/ n)) # mean
print(arr[n//2]) # median

# arr_mode 는 출력이 튜플형식으로 (값, 빈도수) 형태로 출력이 된다.
# 같은 값일 경우 값의 오름차순으로 정렬이 됨을 이용하여 PS를 진행하였다.
# 최빈값이 여러개일때, 두번째로 작은 값을 출력하여야 한다.
arr_mode = Counter(arr).most_common()
if len(arr_mode) > 1:
    if arr_mode[0][1] == arr_mode[1][1]:
        print(arr_mode[1][0])
    else:
        print(arr_mode[0][0])
else:
    print(arr_mode[0][0])

print(arr[n-1] - arr[0]) # range