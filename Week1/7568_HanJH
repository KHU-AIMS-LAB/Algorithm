# 총 몇명을 입력 받을 것인지 먼저 입력 받는다. 
n = int(input())

# 리스트를 정의하고, 리스트에 각 사람의 (몸무게, 키)를 
# 기록한 tuple 형태로 리스트에 append
l = []

for i in range(n):
    info = input()
    weight = int(info.split(' ')[0])
    height = int(info.split(' ')[1])
    dung = (weight, height)
    l.append(dung)


# 각 사람마다 본인을 제외한 상대방들과의 몸무게와 키 비교를 통해서 
# 본인의 rank를 정할 수 있다. 
for i in range(n):
    rank = 1
    for j in range(n):
        if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            rank += 1
    print(rank, end=' ')
