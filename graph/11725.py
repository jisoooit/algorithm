from collections import deque
def bfs(v):
  global visit,g
  q=deque()
  q.append(v)
  visit[v]=1
  while q:
    v=q.popleft()
    # print(x,y)
    for i in s[v]:
      if visit[i]==0:
        visit[i]=1
        arr[i]=v
        q.append(i)
        

n=int(input())
arr=[0 for i in range(n+1)]
s=[[]for i in range(n+1)]
visit=[0 for i in range(n+1)]

for i in range(n-1):
  p,q=map(int,input().split())
  s[p].append(q)
  s[q].append(p)
  #print(p,q)

bfs(1)
for i in range(2,n+1):
  print(arr[i])
