# Test case 입력
test_case = int(input())


for _ in range(test_case):
    # column 개수 입력 받기 
    n_col = int(input())
    s= [] 
    s.append(list(map(int, input().split())))
    s.append(list(map(int, input().split())))
    
    
    # 1번째 경우는 단순히 0번째 인덱스에서 인접하지 않은 것들과 합한 것
    # 이후엔, 각각의 위치에서 서로 다른 행의 전 값과 전전 값을 비교하여 더 큰것과 합해나감. 
    for i in range(1, n_col):
        if i == 1:
            s[0][i] += s[1][i-1]
            s[1][i] += s[0][i-1]
        else:
            s[0][i] += max(s[1][i-1] , s[1][i-2])
            s[1][i] += max(s[0][i-1], s[0][i-2])

    print(max(s[0][n_col-1], s[1][n_col-1]))
