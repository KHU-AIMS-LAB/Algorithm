import sys 
import math 


# stage번째 집에서 R-0, G-1, B-2로 칠할 때의 비용
def dynamic_prog(total_cost_list, cost_list, stage, idx):
    # 한 집만 있는 경우에는 최솟값 출력 
    if stage == 1:
        return cost_list[1][idx]
    # 이전 집까지의 최솟값과 현재 집의 각 색깔마다의 비용을 계산
    else:
        if idx == 0: 
            if total_cost_list[stage-1][1] > total_cost_list[stage-1][2]:
                return total_cost_list[stage-1][2] + cost_list[stage][idx]
            else:
                return total_cost_list[stage-1][1] + cost_list[stage][idx]
        elif idx == 1:
            if total_cost_list[stage-1][0] > total_cost_list[stage-1][2]:
                return total_cost_list[stage-1][2] + cost_list[stage][idx]
            else:
                return total_cost_list[stage-1][0] + cost_list[stage][idx]
        elif idx == 2:
            if total_cost_list[stage-1][0] > total_cost_list[stage-1][1]:
                return total_cost_list[stage-1][1] + cost_list[stage][idx]
            else:
                return total_cost_list[stage-1][0] + cost_list[stage][idx]

    


N = int(input())

cost_list = [[0,0,0] for i in range(N+1)]
total_cost_list = [[0,0,0] for i in range(N+1)]

for i in range(N):
    n_th_cost = sys.stdin.readline().split()
    cost_list[i+1][0] = int(n_th_cost[0])
    cost_list[i+1][1] = int(n_th_cost[1])
    cost_list[i+1][2] = int(n_th_cost[2])



for i in range(1, N+1):
    # print(i)
    total_cost_list[i][0] = dynamic_prog(total_cost_list, cost_list, i, 0)
    total_cost_list[i][1] = dynamic_prog(total_cost_list, cost_list, i, 1)
    total_cost_list[i][2] = dynamic_prog(total_cost_list, cost_list, i, 2)


print(min(total_cost_list[-1]))
