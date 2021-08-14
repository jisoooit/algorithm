from collections import deque

def bfs(x): 
  visit[x]=1 
  q = deque() 
  q.append(x) 
  while q: 
    a = q.popleft() 
    for i in s[a]: 
      
      if visit[i]==0: 
        visit[i] = -1*visit[a] 
        q.append(i) 
      else: 
        if visit[i] == visit[a]:         
          return False 
  return True


k=int(input())
for i in range(k):
  n,m=map(int,input().split())
  s=[[] for i in range(n+1)]
  visit=[0 for i in range(n+1)]
  #color=[0 for i in range(n+1)]
  flg=1
  for i in range(m):
    x,y=map(int,input().split())
    s[x].append(y)
    s[y].append(x)
  

  
  for k in range(1, n+1): 
    if visit[k]==0:
      if not bfs(k): 
        flg = -1 
        break 
  
  print('YES' if flg==1 else 'NO')
