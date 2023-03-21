import sys

n_visit = int(sys.stdin.readline()) # 아이들&거점지 방문 횟수
gift_list = [] # 선물들의 가치 저장

for i in range(n_visit):
    visit_type = list(map(int, sys.stdin.readline().split()))

# 방문 정보에 대한 list 'visit_type'의 길이가 1 == 입력이 0인 경우
# 오름차순으로 정렬된 선물 리스트에서 가장 가치가 큰 선물 pop
# 선물이 없을 경우 -1 출력
    if len(visit_type) == 1:
        try:
            print(gift_list.pop())
        except:
            print(-1)

# 거점지에서 선물을 충전하는 경우
# 선물의 개수인 첫 번째 element를 제외하고 나머지만 선물 리스트에 담은 후 오름차순 정렬
    else:
        gift_list+= visit_type[1:]
        gift_list.sort() # 오름차순
