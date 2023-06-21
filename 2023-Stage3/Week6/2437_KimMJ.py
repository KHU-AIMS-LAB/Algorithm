N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

num = 1

# 정렬 후 최소 1부터 시작

for i in arr:
    if num < i :
        break
    num += i
    #print(num)
print(num)