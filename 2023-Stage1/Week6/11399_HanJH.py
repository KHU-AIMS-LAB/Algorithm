import sys

n = int(sys.stdin.readline().strip())
# 각 사람마다 시간이 얼마나 걸리는 지에 대해서 저장 
time_list = list(map(int, sys.stdin.readline().split()))
time_list.sort()

ans = 0
# 시간이 적게 걸리는 사람부터 먼저
for i in range(len(time_list)):
    ans += time_list[i] * (len(time_list)-i)


print(ans)
