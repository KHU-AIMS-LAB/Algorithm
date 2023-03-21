import sys

N = int(sys.stdin.readline())

my_list = []

for com in range(N):
    command = sys.stdin.readline().strip()

    if 'push' in command:
        my_list.append(command.split(' ')[1])

    elif command == 'top':
        try:
            print(my_list[-1]) # 스택의 top에 있는 정수 출력
        except:
            print(-1)

    # pop()은 내가 지정한 위치의 값을 취득한 후 삭제함
    # 인덱스를 지정하지 않으면 리스트의 마지막 항목을 삭제하고 return함
    elif command == 'pop':
        try:
            print(my_list.pop())
        except:
            print(-1)

    elif command == 'size':
        print(len(my_list))

    elif command == 'empty':
        if my_list:
            print(0)
        else:
            print(1)
