T = int(input())
# 0을 사용한 횟수와 1을 사용한 횟수를 저장할 리스트를 만든다
zero = [0 for _ in range(41)]
one = [0 for _ in range(41)]
# 0을 사용한 횟수를 저장할 zero list 는 0번 index를 1로 설정한다.
zero[0] = 1
# 1을 사용한 횟수를 저장할 one list 는 1번 index를 1로 설정한다.
one[1] = 1

# 각 테스트 케이스에 대해 아래 코드를 실행한다.
for i in range(T):
    t = int(input())

    # 0, 1을 제외한 2부터 카운트
    for i in range(2, t+1):
        # 새로운 피보나치를 만든다
        # zero[2]는 zero[0] + zero[1] / zero[3] 는 zero[1] + zero[2]
        # 마찬가지로  one[2]는 one[0] + one[1] / one[3] 는 one[1] + one[2]
        if zero[i] == 0 and one[i] == 0:
            zero[i] = zero[i-1] + zero[i-2]
            one[i] = one[i-1] + one[i-2]
        else:
            pass

    print(f"{zero[t]} {one[t]}")