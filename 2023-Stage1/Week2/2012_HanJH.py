import sys
import math
from itertools import permutations


# n = int(input())
n = int(sys.stdin.readline().strip())

# 학생들의 예상 등수를 기록할 리스트
student = [0] * n
for i in range(n):
    # expect = int(input())
    expect = int(sys.stdin.readline().strip())
    student[i] = expect
    
# 각 학생들의 예상 점수를 오름차순으로 정렬 
student.sort()
# print(student)
    
"""min_complain = math.inf

for real_order in permutations(range(1, len(student) + 1), len(staudent)):
    complain = 0
    for i in range(n):
        complain += abs(real_order[i] - student[i])
    
    if complain < min_complain : 
        min_complain = complain
        
        
  원래는 permutation을 통해서 학생들의 예상 점수와 실제 등수의 차를 경우의 수마다 구하고, 
  최소값을 구하는 식으로 하려고 했으나, 학생들의 예상 등수를 오름차순으로 정렬하고, 그것들의 인덱스를 실제 등수라고 가정했을 때,
  가장 최소 값이 나온다는 것을 알게 되었다. 
"""
min_complain = 0
for i in range(n):
    # print(abs(i+1 - student[i]))
    min_complain += abs(i+1 - student[i])

        
print(min_complain)
