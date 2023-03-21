import sys

# 총 인원 수
total_ppl = int(sys.stdin.readline())
total_list = list()

# 총 인원 수만큼의 몸무게와 키를 입력받아 tuple로 묶어 list에 저장
for person in range(total_ppl):
    weight, height = map(int, sys.stdin.readline().split())

    total_list.append((weight, height))


# 등수 저장
ranking_score = [1 for i in range(total_ppl)]

"""
1번부터 시작하여 이후 사람들과 몸무게, 키를 비교하면서 덩치 차이를 정의할 수 있을 때
ranking score 업데이트
"""

for i in range(total_ppl): # 기준이 되는 사람 index
    for j in range(i + 1, total_ppl): # 비교 대상 index

        # 1) 기준이 되는 사람의 덩치가 더 큰 경우
        if total_list[i][0] > total_list[j][0]: # i가 j보다 무거울 때
            if total_list[i][1] > total_list[j][1]: # i가 j보다 키가 클 때
                ranking_score[j] += 1 # 비교 대상의 등수 업데이트

        # 2) 비교 대상의 덩치가 더 큰 경우
        elif total_list[i][0] < total_list[j][0]: # i가 j보다 가벼울 때
            if total_list[i][1] < total_list[j][1]: # i가 j보다 키가 작을 때
                ranking_score[i] += 1 # 기준 대상의 등수 업데이트
                

print(*ranking_score)
