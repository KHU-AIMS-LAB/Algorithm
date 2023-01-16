import sys
a = str(sys.stdin.readline())
# sorted : 오름차순, parameter에 reverse를 True로 하면 내림차순!
# sorted 는 분리된채로 list type으로 반환되므로 join을 통해 재결합을 해 주어야 한다.
a = ''.join(sorted(a, reverse=True))
print(a)