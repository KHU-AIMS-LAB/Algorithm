import sys 

n = int(input())

pattern = sys.stdin.readline().strip()
front = pattern.split('*')[0]
rear = pattern.split('*')[1]

for i in range(n):
    file_name = sys.stdin.readline().strip()
    if len(file_name) < (len(front) + len(rear)):
        print('NE')
    else:
        if file_name[:len(front)] == front and file_name[-len(rear):] == rear:
            # print(file_name[:len(front)], ':', front)
            # print(file_name[-len(rear):], ':', rear)
            print('DA')
        else:
            # print(file_name[:len(front)], ':', front)
            # print(file_name[-len(rear):], ':', rear)
            print('NE')
