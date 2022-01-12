from collections import deque
    
def bfs(): 
  q=deque()
  cnt=0
  q.append([s,cnt])
  visit=set([s])
  while q:
    p,cnt=q.popleft()
    if p==g:
      return cnt
    
    if p+u<=f and p+u not in visit:
      visit.add(p+u)
      q.append([p+u,cnt+1])


    if 0<p-d and p-d not in visit:
      visit.add(p-d)
      q.append([p-d,cnt+1])
    
  return "use the stairs"

f,s,g,u,d=map(int,input().split())

ans=0
ans=bfs()

print(ans)



        





