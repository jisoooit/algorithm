from collections import deque

n=int(input())
m=1
k=0

def bfs(x,y):
  global visit,m
  q=deque()
  q.append((x,y))
  visit[x][y]=1
  while q:
    x,y=q.popleft()
    # print(x,y)
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or ny<0 or nx>=n or ny>=n:
        continue
      if g[nx][ny]==0:
        continue
      if g[nx][ny]==1 and visit[nx][ny]==0:
        m+=1
        # print(nx,ny)
        visit[nx][ny]=1
        q.append((nx,ny))



#s=[[0]*(n+1) for i in range(n+1)]
visit=[[0]*(n) for i in range(n)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
x,y=0,0
g=[]
for i in range(n):
  g.append(list(map(int,input())))

arr=[]
for i in range(0,n):
  for j in range(0,n):
    if not visit[i][j] and g[i][j]==1:
      k+=1
      bfs(i,j)
      arr.append(m)
      m=1
arr.sort()
print(k)
for i in arr:
  print(i)
