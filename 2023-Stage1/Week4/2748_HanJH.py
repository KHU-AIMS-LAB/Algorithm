import sys 


n = int(sys.stdin.readline().strip())

# 값을 저장해 놓은 list (0번째 ~ n번째)
fibo_list=[-1] * (n+1)
# 0번째와 1번째는 각각 0과 1로 미리 설정이 되어 있다. 
fibo_list[0] = 0
fibo_list[1] = 1


# 2 ~ n까지 반복 : 값들이 본인의 인덱스보다 작은 경우에는 이미 계산이 되어 있을 것이므로, 해당 값을 참고하고 
# 해당 인덱스에서 새로운 값이 계산이 되면 fibo_list에 저장한다. 
for i in range(2, n+1): 
    fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]

print(fibo_list[-1])
