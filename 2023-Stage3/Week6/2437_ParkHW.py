N = int(input())
nums = list(map(int, input().split()))
# 작은 수부터 사용할 수 있도록 sorting
nums.sort()

# 우선 1을 기준으로 시작함
# 1이 없을 경우에는 최소값을 1로 리턴할 수 있음
result = 1

# 정렬된 리스트를 순회
# 예를 들어, [1, 2, 3] (현재 갖고 있는 추들의 집합, 합6) + [3] (추가될 추)의 상황이 있다고 가정 
# 이처럼 현재의 최소값보다 다음에 추가될 추가 같거나 작은 경우에는 최솟값 ~ 최솟값+추가될추의값 (6~9) 만큼을 모두 커버할 수 있게 됨
# 반대로 최소값보다 다음에 추가될 추가 큰 경우에 커버 불가능으로 판단하고 순회를 멈춤
 
for i in range(0, N):
    if result < nums[i]:
        break
    else:
        result += nums[i]

print(result)
