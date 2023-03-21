import itertools 
import sys

height = [0] * 9
total_height = 0

# 각 난쟁이들의 키를 기록하고, 난쟁이들의 키의 합을 구한다. 
for i in range(9):
    # height[i] = int(sys.stdin.readline())
    height[i] = int(input())
    # print(height[i])
    total_height += height[i]
    
# 2명의 난쟁이를 골라서 총 난쟁이의 키의 합에서 차를 구한다. 
for num_1, num_2 in itertools.combinations(height, 2):
    # print('1', num_1)
    # print('2', num_2)
    seven_height = total_height - num_1 - num_2
    if seven_height == 100:
        # 만약 두 명의 키를 뺐을 떄 100이 된다면, 두명의 인덱스를 별도로 선언하고, for문을 나온다. 
        out_one = num_1
        out_two = num_2
        break 

        
final_list = [0] * 7
idx = 0
# 위에서 구한 값이 아닌 경우에 final_list에 넣어준다. 
for i in range(9):
    if height[i] != out_one and height[i] != out_two:
        final_list[idx] = height[i]
        idx += 1
# 난쟁이의 키를 오름차순으로 정렬한다. 
final_list.sort()

for x in final_list:
    print(x)
    
