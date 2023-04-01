n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])


coin_list = []
payment_case = [0] * (k+1)
# 각 동전들이 처음 시작하기 위한 설정
payment_case[0]=1

for i in range(n):
    coin = int(input())
    coin_list.append(coin)

for coin in coin_list:
    # coin을 돌아가면서 진행 
    # 현재 coin보다 작은 value를 지불하는 방법은 존재하지 않으므로, 내부 for문에서는 coin부터 시작하면 된다. 
    for i in range(coin, k + 1):
        # 해당 값에서 coin을 뺐을때 0이거나, 0보다 작으면 pass
        if i - coin >= 0: 
            # 현재 coin을 하나 지불한다고 했을 때, i - coin을 지불하는 경우의 수를 더해줌. 
            payment_case[i] += payment_case[i-coin]
    
print(payment_case[-1])
