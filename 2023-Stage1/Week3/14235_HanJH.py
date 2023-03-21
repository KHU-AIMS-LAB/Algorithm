import sys

# n = int(input())
n = int(sys.stdin.readline().strip())


present = []
# 굳이 몇번 도는지에 대해서 알 필요가 없으니 i 대신 _를 사용
for _ in range(n):
    # 입력받기 -> 입력을 받아서 띄어쓰기 단위로 split한 리스트
    # santa = list(input().split())
    santa = list(sys.stdin.readline().strip().split())
    
    # 선물 거점지가 아닌 아이들을 만난 경우 
    if santa[0] == '0':
        if len(present) == 0:
            print(-1)
        else:
            print(present.pop())
    
    # 거점지에서 선물을 가져오는 경우 
    else:
        # 입력받은 a의 크기만큼 선물을 present라는 list에 넣고, 마지막에 오름차순으로 정렬한다. 
        for i in range(int(santa[0])):
            present.append(int(santa[i+1]))
        present.sort()    
