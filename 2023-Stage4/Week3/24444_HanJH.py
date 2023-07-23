from collections import deque 
import sys 

N, M, R = map(int, sys.stdin.readline().split())
line = [[] for _ in range(N+1)]
visited = [0] * (N+1)

cnt = 1

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    line[a].append(b)
    line[b].append(a)
    

def bfs(t):
    global cnt 
    
    q = deque([R])
    visited[R] = 1
    
    while q:
        t = q.popleft()
        line[t].sort()
        
        for l in line[t]:
            if visited[l] == 0:
                cnt += 1
                visited[l] = cnt 
                q.append(l)
                
            

bfs(R)

for v in visited[1:]:
    print(v)


    
