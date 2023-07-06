# 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다
# 없어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게되면 또 터지게 된다
# 내려오고 터짐을 반복하면서 1연쇄씩 늘어난다
from collections import deque

fields  = []
results = 0
again = 2

queue = deque([])

for i in range(12):
    field = list(input())
    fields.append(field)

# while 문을 통해, 
# 상하좌우로 같은 알파벳으로 연결된 세트들을 찾고,
# 세트가 존재한다면 그것들을 없앤 다음
# 터뜨리는 과정을 반복해야 한다.

while True:
    # while 문을 계속 반복할 건지 결정하는 변수
    again = 0
    # 없앨 좌표들
    remove = []

    # 모든 좌표를 순회한다
    for i in range(12):
        for j in range(6):
            visit = []
            value = fields[i][j]
            cnt  = 1
            
            # 어떤 좌표의 값이 . 이 아니라면,
            if value != ".":    
                # queue 에 넣고, 방문했음을 표시하기 위해 visit에 넣는다
                queue.append((i, j))
                visit.append((i, j))

            # queue가 비어있을 때까지 아래 과정을 반복한다
            while len(queue) != 0 :
                # queue 의 값을 빼고
                ab = queue.pop()
                a, b = ab[0], ab[1]
                
                # visit 하지 않았다면, 상하좌우를 방문해서 기준 값과 동일한 알파벳인지를 비교한다
                # 만약 동일한 알파벳이라면 또다시 queue를 넣고 visit에도 넣는다
                # 동일한 알파벳을 찾을 때마다 cnt 값을 증가시킨다
                if a != 11 and (a + 1, b) not in visit:
                    if fields[a + 1][b] == value:
                        queue.append((a + 1, b))
                        visit.append((a + 1, b))
                        cnt+=1

                if a != 0 and (a - 1, b) not in visit:
                    if fields[a - 1][b] == value:
                        queue.append((a - 1, b))
                        visit.append((a - 1, b))
                        cnt+=1

                if b != 5 and (a, b + 1) not in visit:
                    if fields[a][b + 1] == value:
                        queue.append((a, b + 1))
                        visit.append((a, b + 1))
                        cnt+=1

                if b != 0 and (a, b - 1) not in visit:
                    if fields[a][b - 1] == value:
                        queue.append((a, b - 1))
                        visit.append((a, b - 1))
                        cnt+=1

            # cnt 가 4이상이라면, 조건이 충족되었으므로 visit 리스트 내의 좌표들을 모두 remove에 넣어준다
            if cnt >= 4:
                for val in visit:
                    remove.append(val)
                again = 1

    # 하나라도 cnt가 4보다 큰 경우가 있었다면, 해당 값들을 모두 .으로 바꿔준다
    if again == 1:
        for val in remove:
            k, m = val[0], val[1]
            fields[k][m] = "."
        results +=1

    # cnt가 4보다 큰 경우가 하나도 없었다면 while 문을 나온다
    elif again != 1:
        break
    
    # 삭제된 공간을 채운다
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if fields[j][i] != "." and fields[k][i] == ".":
                    fields[k][i] = fields[j][i]
                    fields[j][i] = "."

    
print(results)
