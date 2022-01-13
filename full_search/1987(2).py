def dfs(y,x,num):
  global ans
  if ans<num:
    ans=num
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx<c and 0<=ny<r and visit[arr[ny][nx]]==0:
      visit[arr[ny][nx]]=1
      dfs(ny,nx,num+1)
      visit[arr[ny][nx]]=0

dx=[1,0,-1,0]
dy=[0,1,0,-1]
r,c=map(int,input().split())
arr=[list(map(lambda x:ord(x)-65,input())) for i in range(r)]
# visit=[[0 for j in range(c)] for i in range(r)]
visit=[0]*(26)
num=1
ans=0
visit[arr[0][0]]=1
dfs(0,0,num)
print(ans)
