from queue import PriorityQueue
import sys

# priority Queue 사용
que = PriorityQueue()

n = int(sys.stdin.readline())

for _ in range(n):
    a = sys.stdin.readline().rstrip().split()
    if a[0] == '0':
        if que.empty():
            print(-1)
        else:
            print(que.get()[1])
    else:
        for i in range(int(a[0])):
            b = int(a[i+1])
            # 내림차순으로 prioirty queue를 사용하기 위해 튜플로 입력
            que.put((-b, b))