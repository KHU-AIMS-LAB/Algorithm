n = int(input())
# 입력으로 들어온 값 하나만을 계산하기 위해서는 두가지 문제가 발생 
# 1. Recursion Error 
# 2. Overflow Error 

# 이 두 문제를 해결하기 위해서는, 애초에 모든 경우에 대한 것을 미리 계산을 하는 것이다. 
# 계산을 하는 과정에서 미리 15746으로 나눠서 Overflow가 되는 일이 없도록 한다. 
answer_list = [0] * 1000001
answer_list[1] = 1
answer_list[2] = 2

for k in range(3,n+1):
    answer_list[k] = (answer_list[k-1]+ answer_list[k-2])%15746

# 연산이 진행되는 과정은 피보나치 수열과 동일한 방식이다. 
print(answer_list[n])
