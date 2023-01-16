import sys

answer = 0

n = int(sys.stdin.readline())
arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = int(sys.stdin.readline())

# sorting 후 index 마다 순위를 부여했을떄의 불만도를 합하면 해결
arr.sort()

for i in range(n):
    answer += abs(arr[i] - (i + 1))

print(answer)