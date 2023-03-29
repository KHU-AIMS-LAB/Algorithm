T = int(input())

# dp table 생성
for i in range(T):
    score = []
    n = int(input())

    for k in range(2):
        score.append(list(map(int, input().split())))

    score[0][1] += score[1][0]
    score[1][1] += score[0][0]

    # 0번 인덱스와 이전, 2번째 전의 값에서 max
    # 1번 인덱스에서 이전, 2번째 전의 값에서 max 
    for j in range(2, n):
        score[0][j] += max(score[1][j - 1], score[1][j - 2])
        score[1][j] += max(score[0][j - 1], score[0][j - 2])

    # 최종 스코어가 0번, 1번에서 둘 중 더 큰 값을 출력
    print(max(score[0][n - 1], score[1][n - 1]))