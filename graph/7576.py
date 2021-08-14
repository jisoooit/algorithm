from collections import deque

w,h=map(int,input().split())
sum=0
#s=[[0]*(n+1) for i in range(n+1)]
visit=[[0]*(w) for i in range(h)]
dx=[1,0,-1,0]
dy=[0,-1,0,1]
x,y=0,0
q=deque()
g=[]
for i in range(h):
  g.append(list(map(int,input().split())))

for i in range(0,h):
  for j in range(0,w):
    if g[i][j]==1:
      q.append((i,j))
      visit[i][j]=1

while q:
    y,x=q.popleft()
    # print(y,x)
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or ny<0 or nx>=w or ny>=h:
        continue
      # if g[ny][nx]==0:
      #   continue
      if g[ny][nx]==0 and visit[ny][nx]==0:
        visit[ny][nx]=visit[y][x]+1
        q.append((ny,nx))
    
for i in range(0,h):
  for j in range(0,w):
   sum=max(sum,visit[i][j])

sum-=1 #1인수의 visit초기값을 1로 잡아서그럼

for i in range(h): #다끝나고 안방문되어있는건 방문 못하는거임
  for j in range(w):
    if g[i][j]==0 and visit[i][j]==0:
      sum=-1
print(sum)
