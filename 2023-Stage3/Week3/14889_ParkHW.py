from itertools import combinations

N = int(input())
mats = list()

# 능력치 matrix를 채워준다
for i in range(0, N):
    mat = list(map(int, input().split()))
    mats.append(mat)

# 최소 차잇값을 저장해줄 변수
min_score = 9999999

# N 명의 사람을 두 팀으로 나누기 위해서 combinations 을 사용한다.
# combinations의 output은 양 끝이 한 세트라고 볼 수 있다. ex) [0, 1, 2] + [3, 4, 5] (이것이 분할의 한 세트) 
# 양끝에서부터 리스트의 중간으로 들어오면서 세트가 구성된다.
c = list(combinations(range(0, N), N//2))
c1 = c[: len(c)//2]
c2 = c[len(c)//2 :]
c2 = c2[::-1] # 고로, 반으로 쪼갰을 때의 2번째 리스트는 reverse 처리해준다.

# 가능한 조합을 순회하며, 이번에는 각 팀에서의 능력치를 계산한다.
for i in range(0, len(c1)):
    sub_score_1 = 0
    # 팀에서 2명씩 묶었을 때의 조합을 또 한 번 계산한다.
    sub_c_1 = list(combinations(c1[i], 2))
    # 능력치의 합을 계산한다.
    for set_1 in sub_c_1:
        sub_score_1 += (mats[set_1[0]][set_1[1]] + mats[set_1[1]][set_1[0]])
    
    sub_score_2 = 0
    sub_c_2 = list(combinations(c2[i], 2))
    for set_2 in sub_c_2:
        sub_score_2 += (mats[set_2[0]][set_2[1]] + mats[set_2[1]][set_2[0]])
    
    # 두 팀의 능력치의 차가 가장 적은 값을 계산한다.
    if abs(sub_score_1 - sub_score_2) < min_score:
        min_score = abs(sub_score_1 - sub_score_2)

print(min_score)