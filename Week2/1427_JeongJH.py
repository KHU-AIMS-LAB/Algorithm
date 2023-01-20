import sys

# 정렬할 값 입력 후 string으로 저장
N = str(sys.stdin.readline().strip())

# sorted() function으로 N에 저장된 숫자배열 정렬하여 list에 저장
sorted_N = sorted(N, reverse = True)

# ''.join()으로 list 내 요소들 사이에 구분자('')를 넣어 반환
print(''.join(sorted_N))
