from collections import deque

def bfs(y,x):
  global visit,g
  q=deque()
  q.append((x,y))
  visit[y][x]=1
  while q:
    x,y=q.popleft()
    # print(x,y)
    for i in range(8):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or ny<0 or nx>=w or ny>=h:
        continue
      if g[ny][nx]==0:
        continue
      if g[ny][nx]==1 and visit[ny][nx]==0:
        visit[ny][nx]=1
        q.append((nx,ny))

while True:
  w,h=map(int,input().split())
  sum=0
  if w==0 and h==0:
    break
#s=[[0]*(n+1) for i in range(n+1)]
  visit=[[0]*(w) for i in range(h)]
  dx=[1,1,0,-1,-1,-1,0,1]
  dy=[0,1,1,1,0,-1,-1,-1]
  x,y=0,0
  g=[]
  for i in range(h):
    g.append(list(map(int,input().split())))

  # for i in range(h):
  #   for j in range(w):
  #     # print(g[i][j],end=' ')
  #     print("인뎃스", i,j)
  #   print()

  for i in range(0,h):
    for j in range(0,w):
      if visit[i][j]==0 and g[i][j]==1:
        sum+=1
        bfs(i,j)
      
  print(sum)
