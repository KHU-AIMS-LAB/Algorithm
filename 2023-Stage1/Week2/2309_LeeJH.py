import sys
arr = [0 for _ in range(9)]

for i in range(9):
    arr[i] = int(sys.stdin.readline())

answer_idx = [0,1,2,3,4,5,6,7,8]
sum = 0
not1 = 0
not2 = 0

arr.sort()

for i in range(9):
    sum += arr[i]

# Combination으로 생각, 9개중 2개를 뺴고 합산이 100이 되는 경우를 찾기
# 100이 되는 순간 빠진 2개의 index를 기록하고 이후 list에서 index 제거
for i in range(8):
    for j in range(1, 9):
        if i == j:
            continue
        elif not1 != 0 & not2 !=0:
            break
        else:
            if (sum - (arr[i] + arr[j])) == 100:
                not1 = i
                not2 = j
                break

answer_idx.remove(not1)
answer_idx.remove(not2)

for i in answer_idx:
    print(arr[i])