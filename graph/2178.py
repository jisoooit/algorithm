from collections import deque

def bfs(y,x):
  global visit,g
  q=deque()
  q.append((x,y))
  visit[y][x]=1
  while q:
    x,y=q.popleft()
    # print(x,y)
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or ny<0 or nx>=w or ny>=h:
        continue
      # if g[ny][nx]==0:
      #   continue
      if g[ny][nx]==1 and visit[ny][nx]==0:
        visit[ny][nx]=visit[y][x]+1
        q.append((nx,ny))


h,w=map(int,input().split())
sum=0
#s=[[0]*(n+1) for i in range(n+1)]
visit=[[0]*(w) for i in range(h)]
dx=[1,0,-1,0]
dy=[0,-1,0,1]
x,y=0,0
g=[]
for i in range(h):
  g.append(list(map(int,input())))

bfs(0,0)

print(visit[h-1][w-1])
