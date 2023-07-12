N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

# 지금까지의 저장된 수를 카운트할 변수
cnt = 0
# K 번째 저장된 수를 저장할 변수
result = -1

# 병합정렬 함수
def merge_sort(A):
    # 리스트의 크기가 1이면 그냥 return 한다
    if len(A) <= 1 : 
        return A

    # 중간 지점을 기준으로 왼쪽 / 오른쪽으로 쪼개준다.
    # 이때, 중간 지점은 len(A) + 1을 기준으로 나눈다.
    mid = (len(A) + 1) // 2
    left = A[:mid]
    right = A[mid:]

    # 왼쪽과 오른쪽에 대해 또다시 병합정렬 함수를 재귀적으로 실행시킨다.
    res_left = merge_sort(left)
    res_right = merge_sort(right)

    # 최종적으로는 두 리스트가 병합되면서 정렬이 된다.
    return merge(res_left, res_right)

# 병합 함수
def merge(left, right):
    global result, cnt

    # 왼쪽을 순회할 i , 오른쪽을 순회할 j , 전체를 순회할 k 변수 생성
    i, j, k = 0, 0, 0
    sorted = []

    # i 가 len(left) 보다 작고 j 가 len(right) 보다 작을때 아래 함수 실행
    while i < len(left) and j < len(right):
        # left[i]와 right[j]를 비교하여 작은 것부터 순서대로 sorted에 append 한다.
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1

    # j는 len(right)보다 크거나 같고, i가 len(left) 보다 작을 때,
    while i < len(left) :
        # sorted 함수에 left[i]를 차례대로 붙인다.
        sorted.append(left[i])
        i += 1
    # 반대도 동일 하게 실행
    while j < len(right):
        sorted.append(right[j])
        j += 1

    # sorted 가 다 계산 되었으면, 저장 개수를 카운트하기 위해 아래 함수를 돌린다.
    # k는 sorted를 순회하고, cnt가 K와 같아지는 순간 result 에 sorted[k]를 저장한다.
    while k < len(sorted):
        cnt += 1

        if cnt == K:
            result = sorted[k]

        k += 1

    return sorted

merge_sort(A)
print(result)