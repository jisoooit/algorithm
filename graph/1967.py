from collections import deque

def init():
  for i in range(n+1):
    visit[i]=0

def bfs(v): #이때의 bfs는 가장 먼 노트와 그 거리를 찾아쥬는 함수
  dist,node=0,0
  q=deque()
  q.append((v,0))
  visit[v]=1
  while q:
    v,v_dist=q.popleft()
    # print(x,y)
    for i in s[v]:
      if visit[i[0]]==0: #튜플 첫번째 원소
        visit[i[0]]=1
        q.append((i[0],v_dist+i[1]))
        if v_dist+i[1]>dist:
          dist=v_dist+i[1]
          node=i[0]
          
  
  return dist,node
  
        

n=int(input())

s=[[] for i in range(n+1)]
visit=[0 for i in range(n+1)]

for i in range(1,n):
  arr=list(map(int,input().split()))
  s[arr[0]].append((arr[1],arr[2]))
  s[arr[1]].append((arr[0],arr[2]))
  # for j in range(1,len(arr),2):
  #   s[arr[0]].append((arr[j],arr[j+1]))

a,b=bfs(1)
init()
print(bfs(b)[0])
