N, K = map(int, input().split())
multitap = list(map(int, input().split()))

plug = []
count = 0

for i in range(K) :
    # 전기 용품이 꽂혀있으면 pass
    if multitap[i] in plug :
        continue
 
    # 빈 곳이 있으면 꽂기
    if len(plug) < N :
        plug.append(multitap[i])
        continue
  
    multitap_idx = []
    hasplug = True

    for j in range(N) :
        # index 저장
        if plug[j] in multitap[i:] :
            idx = multitap[i:].index(plug[j])
        else:
            idx = 101
            hasplug = False

        multitap_idx.append(idx)
    
        # 끝나면 종료
        if not hasplug :
            break

    # 플러그 뽑기
    plug_out = multitap_idx.index(max(multitap_idx))
    plug.pop(plug_out)
    plug.append(multitap[i])
    count += 1

print(count)