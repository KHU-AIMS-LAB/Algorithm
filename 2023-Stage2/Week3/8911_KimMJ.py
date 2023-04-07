T = int(input())
way = []

for i in range(T):
    way.append(input())
    
for i in range(len(way)):
    # x,y 좌표 및 방향을 0으로 초기화
    x, y, direction = 0, 0, 0
    # x, y 좌표 값 리스트
    x_value, y_value = [0], [0]
    for j in range(len(way[i])):
        # 북쪽 : 0, 동쪽 : 1, 남쪽 : 2, 서쪽 : 3
        if (direction == 0 and way[i][j] == 'F') or (direction == 2 and way[i][j] =='B'):
            y += 1
        elif (direction == 0 and way[i][j] =='B') or (direction == 2 and way[i][j] =='F'):
            y -= 1
        elif (direction == 1 and way[i][j] =='F') or (direction == 3 and way[i][j] =='B'):
            x += 1
        elif (direction == 1 and way[i][j] =='B') or (direction == 3 and way[i][j] =='F'):
            x -= 1    
        elif way[i][j] == 'L':
            direction = (direction - 1) % 4
        elif way[i][j] == 'R':
            direction = (direction + 1) % 4

        x_value.append(x)
        y_value.append(y)

    print((max(x_value) - min(x_value)) * (max(y_value) - min(y_value)))
