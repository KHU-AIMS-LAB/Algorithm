import sys 


n = int(sys.stdin.readline().strip())
# n = int(input())

# 0 ~ n번째 계단에서 가질 수 있는 점수의 최대 합과 그때 연속된 계단을 몇개 올랐는지를 저장하는 list 
# 2차원으로 저장하여 0번째 column에서는 연속 레벨이 1인 지점, 1번째 column에서는 연속 레벨이 2인 지점에서의 점수의 최댓값을 저장 
score_list = []
for i in range(n+1):
    score_list.append([0,0,0])


# 각 계단에서의 점수 값을 입력받아 저장한다. 
stage_score = [0] * (n+1) 
for i in range(1, n + 1):
    stage_score[i] = int(sys.stdin.readline().strip())
    # stage_score[i] = int(input())

# 계단이 1개인 경우 
if n == 1:
    print(stage_score[1])
# 계단이 2개인 경우 
elif n == 2:
    print(stage_score[1] + stage_score[2])
# 계단이 3개인 경우
else:

    # 처음시작할 때는 0점
    score_list[0][0] = 0
    score_list[0][1] = 0
    score_list[0][2] = 0
    # 첫번째 계단에서 연속 레벨이 0, 1, 2인 지점
    score_list[1][0] = 0
    score_list[1][1] = stage_score[1]
    score_list[1][2] = 0
    # 두번째 계단에서 가질 수 있는 최대 점수 
    score_list[2][0] = 0
    score_list[2][1] = stage_score[2]
    score_list[2][2] = stage_score[1] + stage_score[2]



    for x in range(3, n+1): # x번째 계단에서 연속 레벨이 1일때의 최댓값과 연속 레벨이 2일때의 최댓값을 각각 저장 

        # 연속 레벨이 1인 경우 : 무조건 2계단 이전에서 올라와야 한다. 2계단 이전에서 더 높은 값을 가지는 것과 stage score를 더한 값이 저장됨
        if score_list[x-2][1] > score_list[x-2][2]: 
            score_list[x][1] = score_list[x-2][1] + stage_score[x]
        elif score_list[x-2][1] <= score_list[x-2][2]:
            score_list[x][1] = score_list[x-2][2] + stage_score[x]

        # 연속 레벨이 2인 경우 : 1계단 이전에서 올라와야 한다. 1계단 이전에서는 연속 레벨이 1인 경우만 올라올 수 있다. 
        score_list[x][2] = score_list[x-1][1] + stage_score[x]

    if score_list[-1][1] > score_list[-1][2]:
        print(score_list[-1][1])
    else : 
        print(score_list[-1][2])
        
        
  # score_list에서 0번째 column은 굳이 안 만들어도 되는 값을 만들었다. 
  
