

def dfs(y,x,idx): 

  #이미 체크한 경우
  if visit[y][x][idx]!=-1:
    return visit[y][x][idx]

  # arr2문자와 일치하지 않는 경우
  if arr[y][x]!=arr2[idx]:
    visit[y][x][idx]=0
    return 0
  
  #찾는 문자와 일치하는 경우
  if idx==len(arr2)-1:
    return 1
  
  cnt=0
  for i in range(-k,k+1):
    if not i:
      continue
    nx,ny=x+i,y+i
    if 0<=nx<m:
      cnt+=dfs(y,nx,idx+1)
    if 0<=ny<n:
      cnt+=dfs(ny,x,idx+1)
  
  visit[y][x][idx]=cnt
  return visit[y][x][idx]

n,m,k=map(int,input().split())
arr = [list(input()) for i in range(n)] #문자열 하나하나 나누려면 split안해도 된다. 
arr2=list(input())


dx=[1,-1,0,0]
dy=[0,0,1,-1]

ans=0
visit=[[[-1]*len(arr2) for _ in range(m)]for _ in range(n)]
for i in range(n):
  for j in range(m):
    if arr[i][j]==arr2[0]:
      ans+=dfs(i,j,0)

print(ans)



        





