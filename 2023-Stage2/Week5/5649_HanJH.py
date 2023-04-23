import math

# fitting line을 계산하는 코드 
def line_of_best_fit(points):
    n = len(points)
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x_squared = 0

    for point in points:
        x = point[0]
        y = point[1]
        sum_x += x
        sum_y += y
        sum_xy += x * y
        sum_x_squared += x ** 2

    a = ((n * sum_xy) - (sum_x * sum_y)) / ((n * sum_x_squared) - (sum_x ** 2))
    b = (sum_y - (a * sum_x)) / n

    return a, b



N = int(input())
point_list = []
for i in range(N):
    point = input().split()
    point_list.append((int(point[0]), int(point[1])))

# print(point_list)
   

# Example usage:

a, b = line_of_best_fit(point_list)
print("{:.3f}".format(a))
print("{:.3f}".format(b))