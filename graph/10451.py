from collections import deque

def bfs(v):
  q=deque([v])
  visit[v]=1
  while q:
    v=q.popleft()
    #print(v, end=' ')
    for i in s[v]:
      if visit[i]==0:
        q.append(i)
        visit[i]=1

k=int(input())

for i in range(k):
  num=0
  n=int(input())
  s=[[] for i in range(n+1)]
  visit=[0 for i in range(n+1)]
  arr=list(map(int,input().split()))
  for i in range(1,n+1):
    s[i].append(arr[i-1])
  
  for i in range(1,n+1):
    if not visit[i]:
      bfs(i)
      num+=1
  
  print(num)
