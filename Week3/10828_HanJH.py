import sys

# N을 입력받는다. 
# n = int(input())
n = int(sys.stdin.readline().strip())


stack = []
for i in range(n):
    # stack이라는 리스트에 아무것도 없는지 확인
    is_empty = len(stack) == 0
    # command = input()
    command = sys.stdin.readline().strip()
    if len(command.split()) == 1:
        if command == "top":
            # top의 명령어를 입력받았을 때, 수행하는 코드 
            if is_empty:
                print(-1)
            else:
                print(stack[-1])
        elif command == 'size':
            # size 
            print(len(stack))
        elif command == 'pop':
            # pop
            if is_empty:
                print(-1)
            else:
                print(stack[-1])
                del stack[-1]
                
        elif command == 'empty':
            # empty
            if is_empty:
                print(1)
            else:
                print(0)
            
    else:
        command = command.split()
        # command에서 뒤에 숫자가 나오는 경우는 push 밖에 없다. 
        stack.append(command[1])
        
        
# sys.stdin.readline()으로 입력을 받을 때, strip()함수를 써야 입력의 가장 뒤에 \n이 붙지 않는다는 것에 주의!
