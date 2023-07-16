def MergeSort(arr):
    if len(arr) <= 1 :
        return arr
    mid = (len(arr) + 1) // 2
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])
    return Merge(left, right)
        
def Merge(left, right):
    global count, result
    i, j, t = 0, 0, 0
    temp = []
    while (i < len(left)) & (j < len(right)) :
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
        
    while i < len(left):
        temp.append(left[i])
        i += 1
    while j < len(right):
        temp.append(right[j])
        j += 1
    
    while t < len(temp):
        count += 1
        if count == K:
            result = temp[t]
        t += 1
        
    return temp
            
N, K = map(int, input().split())
arr =  list(map(int, input().split()))

count = 0
result = -1
MergeSort(arr)
print(result)