N, total = map(int, input().split())
value = []

for i in range(N):
    value.append(int(input()))

# 초기화
result = [0] * (total + 1)

# value 정렬
value.sort()

for i in value:
    for j in range(total + 1):
        #i원으로만 total을 채울 수 있는 경우
        if j % i == 0 and result[j] == 0:
            result[j] = 1

        # i원을 더해도 total을 넘지 않으면 경우 추가
        if i + j <= total :
            result[i + j] += result[j]

print(result[-1])
