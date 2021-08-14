from collections import deque

n,m=map(int,input().split())
s=[[0]*(n+1) for i in range(n+1)]
visit=[0 for i in range(n+1)]
num=0

def dfs(v):
  visit[v]=True
  #print(v, end=' ')
  for i in range(1,n+1):
    if not visit[i] and s[v][i]==1:
      dfs(i)

def bfs(v):
  q=deque([v])
  visit[v]=True
  while q:
    v=q.popleft()
    for i in range(1,n+1):
      if not visit[i] and s[v][i]==1:
        q.append(i)
        visit[i]=True


for i in range(m):
  x,y=map(int,input().split())
  s[x][y]=1
  s[y][x]=1


for i in range(1,n+1):
  if not visit[i]:
    bfs(i)
    num+=1
print(num)
