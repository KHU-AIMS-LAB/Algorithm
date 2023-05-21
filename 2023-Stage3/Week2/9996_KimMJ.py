N = int(input())
pattern = input().split('*')

for _ in range(N) :
    file = input()
    # 패턴의 별표 전과 파일의 첫 부분이 같은지, 패턴의 별표 후와 파일의 끝부분이 같은지 확인
    if pattern[0] == file[0: len(pattern[0])] and pattern[1] == file[len(pattern[0]):][-len(pattern[1]):] :
        print("DA")
    else :
        print("NE")