import sys 

# n을 입력받는다. 
n = int(sys.stdin.readline().strip())
# n = int(input())


# n이 1인 경우 
if n == 1:
    print(1)
# n이 2인 경우
elif n == 2:
    print(3)
# n이 3보다 큰 경우
# solution_list[i] = solution_list[i-1] + 2 * solution_list[i-2]
else:
    solution_list = [0] * (n+1)

    solution_list[1] = 1
    solution_list[2] = 3

    for i in range(3, n+1):
        solution_list[i] = solution_list[i-1] + 2 * solution_list[i-2]

    print(solution_list[-1] % 10007)
