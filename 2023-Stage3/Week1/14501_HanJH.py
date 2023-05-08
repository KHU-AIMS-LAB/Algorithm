import sys 


N = int(input())
t_list = [0] * (N + 1)
p_list = [0] * (N + 1)

for i in range(N):
    t, p = map(int, sys.stdin.readline().split())
    t_list[i+1] = t
    p_list[i+1] = p

# print(t_list)
# print(p_list)


result_list = [0] * (N+2)

# 거꾸로 진행한다. 
# f(x) : x일 이후에 얻을 수 있는 최대 수익 
#  

for i in range(N):
    # 가장 마지막 날짜의 t의 값이 1이면 해당 p값을 설정하고, 
    # t의 값이 1이 아니라면, 0이다. 
    if i == 0:
        if t_list[N-i] == 1:
            result_list[N-i] = p_list[N-i]
        # 1이 아닌 경우에는 0이 되어야 하는데, 이미 0으로 초기화되었으므로, 굳이 해줄 필요 없음 
    
    
    
    else:
        # 해당 날짜에 계획되어 있는 상담을 잡는 경우, 그리고 상담이 t일 필요하다고 할 때, 
        # 해당 날짜 상담에 대한 비용과 t일 이후에 얻을 수 있는 최대 비용을 더한 것과 
        # 해당 날짜 상담을 하지 않고 넘어가는 경우 (t + 1일 이후에 얻을 수 있는 최대 비용)
        # 비교하여 더 큰 값을 설정한다. 

        # 하지만, t일 이후가 N보다 큰 경우에는 해당 날짜에 상담을 진행할 수 없다. 
        duration = t_list[N - i]
        if N - i + duration > N+1:
            result_list[N-i] = result_list[N-i+1]
        else:
            price = p_list[N- i]
            if result_list[N-i+1]  >  price + result_list[N - i + duration] : 
                result_list[N-i] = result_list[N-i+1]
            else:
                result_list[N-i] = price + result_list[N - i + duration]

print(result_list[1])

