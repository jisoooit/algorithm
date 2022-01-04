from collections import deque

def bfs():
  q=deque()
  q.append(n)
  while q:
    p=q.popleft()
    if p==k:
      print(dist[p])
      break
    for i in (p-1,p+1,2*p):
      if 0<=i<=100000 and dist[i]==0:
        q.append(i)
        dist[i]=dist[p]+1

n,k=map(int,input().split())
dist=[0]*(100000+1)
bfs()





