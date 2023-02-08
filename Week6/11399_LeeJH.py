import sys

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))
arr.sort()

answer = 0

# 오름차순으로 정렬후 각 index별로 시간 x 남은 사람의 수를 하면 해결
for i in range(n):
    answer += arr[i] * (len(arr) - i)

print(answer)