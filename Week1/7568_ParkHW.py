# 케이스의 갯수 N을 입력받음
N = int(input())

# weights, heights, rank를 저장할 list 를 만들어줌
weights  = [0] * N
heights  = [0] * N
rank = [0] * N

# N 개 만큼 weight, height 를 입력 받아서 각 list에 넣어둠
for i in range(0, N):
    x, y = input().split()
    x = int(x)
    y = int(y)
    weights[i] = x
    heights[i] = y

# 2중 for문을 통한 weight, height 리스트 순회
# i보다 weight와 height 가 모두 큰 사람의 수를 구하여 rank를 계산
for i in range(0, N):
    # 나보다 덩치가 큰 사람이 없을 때의 rank = 1이므로 초기값 (temp) 1로 설정
    temp = 1
    for j in range(0, N):
        if i != j:
            # 나보다 weight, height 모두 큰 사람을 발견할 때마다 temp + 1
            if weights[i] < weights[j]:
                if heights[i] < heights[j]:
                    temp+=1

    # 최종 temp값을 rank에 넣어줌
    rank[i] = temp
    print(rank[i], end=" ")
    

