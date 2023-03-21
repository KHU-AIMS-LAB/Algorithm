import sys 
# n, k 입력 받음
nk = sys.stdin.readline().strip()
n = int(nk.split()[0])
k = int(nk.split()[1])

# 동전을 list에 저장 
coin_list = [0] *n 
for i in range(n):
    coin = int(sys.stdin.readline().strip())
    coin_list[i] = coin


coin_list.sort(reverse=True)
# print(coin_list)


coin_num = 0

for i in range(n):
    if k == 0:
        break 
    else:
        num = k // coin_list[i]
        rest = k % coin_list[i]
        coin_num += num
        k = rest

print(coin_num)
