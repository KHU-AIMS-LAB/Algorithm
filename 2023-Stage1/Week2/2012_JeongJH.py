import sys

N = int(sys.stdin.readline()) # 총 학생 수
expect_rank = [int(sys.stdin.readline().strip()) for i in range(N)] # 예상 등수 리스트


#1등부터 N등까지 동석차 없이 등수를 매겨야 하므로 실제 등수는 1~N 리스트
#불만도를 최소로 하려면 학생이 적어낸 예상 등수 리스트를 오름차순으로 정렬한 뒤
#실제 등수와 예상 등수에서 동일한 인덱스에 위치한 요소끼리 매칭되어야 함

real_rank = [i+1 for i in range(N)]
expect_rank.sort()
complaint = [abs(exp - real) for exp, real in zip(expect_rank, real_rank)]


print(sum(complaint))
