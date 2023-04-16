N = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))
min_val, max_val = 1000000000, -1000000000

result = num[0]

def DFS(idx):
    global result, min_val, max_val

    # 마지막 index에서 최대 최소 비교
    if idx == N:
        if result < min_val:
            min_val = result        
        if result > max_val:
            max_val = result
        return

    # 연산 후 DFS
    for i in range(4):
        temp = result
        if operator[i] > 0:
            if i == 0:
                result += num[idx]
            elif i == 1:
                result -= num[idx]
            elif i == 2:
                result *= num[idx]
            else:
                result = int(result / num[idx])
            operator[i] -= 1
            DFS(idx + 1)
            operator[i] += 1            
            result = temp

DFS(1)
print(max_val)
print(min_val)