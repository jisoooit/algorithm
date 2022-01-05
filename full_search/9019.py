from collections import deque
t=int(input())

visited=[0]*(10000)

def bfs(n):
  q=deque()
  store=''
  q.append([n,store])
  while q:
    num,store=q.popleft()
    visited[num]=1
    if num==m:
      return store
   
    l = num % 1000 * 10 + num // 1000
    r = num % 10 * 1000 + num // 10
    if visited[num*2%10000]==0:
      visited[num * 2 % 10000] = 1
      q.append([num*2%10000,store+'D'])
    if visited[num-1]==0:
      if(num==0):
        visited[9999] = 1
        q.append([9999,store+'S'])
      else:
        visited[num-1] = 1
        q.append([num-1,store+'S'])
    if visited[l]==0:
      visited[l] = 1
      q.append([l,store+'L'])
    if visited[r]==0:
      visited[r] = 1
      q.append([r,store+'R'])
  return store
    

for i in range(t):
  n,m=map(int,input().split())
  #n_list = list(map(int, str(n)))
  print(bfs(n))
  visited=[0]*(10000)
