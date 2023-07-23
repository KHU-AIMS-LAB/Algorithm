n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    first = 0
    second = 1 

    for i in range(n - 1): 
        third = first + second
        first = second 
        second = third


    print(third)
