import sys

dwarf = 9 # 난쟁이 수
age_list = [int(sys.stdin.readline().strip()) for i in range(dwarf)] # 난쟁이 나이 저장

breaker = False # 이중 for문에서 나오기 위한 변수

# list에서 일곱 난쟁이의 키 합이 100인 경우가 발생하면 for문 탈출
for i in range(dwarf):
    for j in range(i+1, dwarf):
        if sum(age_list) - (age_list[i] + age_list[j]) == 100:
            del age_list[j]
            del age_list[i]
            age_list.sort()
            print(*age_list)
            
            breaker = True 
            break

    if breaker == True:
        break
