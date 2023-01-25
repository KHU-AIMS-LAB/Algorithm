import sys 


# 숫자를 입력 받는다 (string 형태로)
number = sys.stdin.readline().strip()
# number = input()

# 받은 String을 list 함수에 넣어주면 문자 하나를 요소로 가지는 list가 생성된다. 
number_list = list(number)

# 리스트를 내림차순으로 정렬 
number_list.sort(reverse=True)

# 리스트의 요소들을 출력
for num in number_list:
    print(num, end='')
