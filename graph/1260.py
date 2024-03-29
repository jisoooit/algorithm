#array = [[0]*11 for i in range(10)] -> 11열 10행 리스트임
#a = [[0 for j in range(2)] for i in range(3)]->[[0,0],[0,0],[0,0]]
from collections import deque

n,m,v=map(int,input().split())
s=[[0]*(n+1) for i in range(n+1)]
visit=[0 for i in range(n+1)]

def dfs(v):
  visit[v]=True
  print(v, end=' ')
  for i in range(1,n+1):
    if not visit[i] and s[v][i]==1:
      dfs(i)

def bfs(v):
  q=deque([v])
  visit[v]=True
  while q:
    v=q.popleft()
    print(v,end=' ')
    for i in range(1,n+1):
      if not visit[i] and s[v][i]==1:
        q.append(i)
        visit[i]=True


for i in range(m):
  x,y=map(int,input().split())
  s[x][y]=1
  s[y][x]=1


for i in range(n+1):
  for j in range(n+1):
    print(s[i][j],end=' ')
  print()
dfs(v)
print()
visit=[0 for i in range(n+1)]
bfs(v)
