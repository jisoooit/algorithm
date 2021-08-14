k=int(input())

def dfs(v):
  global ans
  visit[v]=1
  team.append(v)
  n=arr[v]
  if visit[n]:
    if n in team:
      ans+=team[team.index(n):]
      print("ans: ",ans)
    return
  else:
    dfs(n)
  


for i in range(k):
  n=int(input())
  m=n
  s=[[]for i in range(n+1)]
  visit=[0 for i in range(n+1)]
  visit[0]=1
  arr=[0]+list(map(int,input().split()))
  ans=list()
  
  for i in range(1,n+1):
    if not visit[i]:
      team=[]
      dfs(i)
      # print()
  print(n-len(ans))
