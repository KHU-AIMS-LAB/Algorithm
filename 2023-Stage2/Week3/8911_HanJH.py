from operator import add

def left_rotate(l):
        rotate_l = []
        rotate_l.append(-l[1])
        rotate_l.append(l[0])

        return rotate_l 


def right_rotate(l):
    rotate_l = []
    rotate_l.append(l[1])
    rotate_l.append(-l[0])
    return rotate_l


test_case = int(input())

for _ in range(test_case):
    # 초기 거북이는 (0, 0)에서 시작 
    pos = [0, 0]

    # 입력
    command_list = input()

    # x좌표와 y좌표의 최댓값 최솟값 초기화 및 선언 
    x_min = 0
    x_max = 0 
    y_min = 0
    y_max = 0

    forward = [0, 1]
    backward = [0, -1]
   

    for command in command_list:
        if command == 'F':
            # Forward 했을 때의 위치로 update
            pos = list(map(add, pos, forward))
            if pos[0] < x_min:
                x_min = pos[0]
            if pos[0] > x_max : 
                x_max = pos[0]
            if pos[1] < y_min:
                y_min = pos[1]
            if pos[1] > y_max:
                y_max = pos[1]
        elif command == 'B':
            # Backward 했을 때의 위치로 update
            pos = list(map(add, pos, backward))
            if pos[0] < x_min:
                x_min = pos[0]
            if pos[0] > x_max : 
                x_max = pos[0]
            if pos[1] < y_min:
                y_min = pos[1]
            if pos[1] > y_max:
                y_max = pos[1]

        elif command == 'L':
            # Forward 변환 
            forward = left_rotate(forward)
            # Backward 변환 
            backward = left_rotate(backward)
            
        elif command == 'R':
            # Forward 변환 
            forward = right_rotate(forward)
            # Backward 변환 
            backward = right_rotate(backward)



    x_len = x_max - x_min
    y_len = y_max - y_min

    print(x_len * y_len)


