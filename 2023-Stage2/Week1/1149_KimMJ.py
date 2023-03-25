N = int(input())
rgb = []
for i in range(N):
    rgb.append(list(map(int, input().split())))

i = 1
while i < N:
    rgb[i][0] = min(rgb[i][0] + rgb[i-1][1], rgb[i][0] + rgb[i-1][2])
    rgb[i][1] = min(rgb[i][1] + rgb[i-1][0], rgb[i][1] + rgb[i-1][2])
    rgb[i][2] = min(rgb[i][2] + rgb[i-1][0], rgb[i][2] + rgb[i-1][1])
    i += 1

print(min(rgb[-1]))