import sys

n = int(sys.stdin.readline())

stack = []
top_idx = -1
stack_size = 0

# 진짜 기본적인 스택구현
for _ in range(n):
    commend = list(sys.stdin.readline().split())
    if commend[0] == "push":
        element = commend[1]
        stack_size += 1
        stack.append(element)
        top_idx += 1
    elif commend[0] == "pop":
        if stack_size == 0:
            print(-1)
            continue
        print(stack[top_idx])
        stack.pop()
        stack_size -= 1
        top_idx -= 1
    elif commend[0] == "size":
        print(stack_size)
    elif commend[0] == "empty":
        if stack_size == 0:
            print(1)
        else:
            print(0)
    elif commend[0] == "top":
        if stack_size == 0:
            print(-1)
        else:
            print(stack[top_idx])