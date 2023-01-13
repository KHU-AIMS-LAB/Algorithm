a = int(input())
b = int(input())
c = int(input())

s_abc = str(a * b * c)

blank = [0,0,0,0,0,0,0,0,0,0]

for i in s_abc:
    blank[int(i)] += 1
for i in range(10):
    print(blank[i])