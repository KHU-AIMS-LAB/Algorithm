import sys
input = sys.stdin.readline

N = int(input())
arr = []

# index도 같이 append
for i in range(N):
    arr.append((int(input()), i))

sort = sorted(arr)
result = []

# sort 횟수
for i in range(N):
    result.append(sort[i][1] - arr[i][1])
    
print(max(result) + 1)