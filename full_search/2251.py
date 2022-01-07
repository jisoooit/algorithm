from collections import deque

def func(x,y):
 if visit[x][y]!=1:
    visit[x][y]=1
    q.append([x,y])

    
def bfs(): 
  q.append([0,0])
  visit[0][0]=1
  while q:
    a1,b1=q.popleft()
    c1=c-a1-b1

    if a1==0:
      result.append(c1)
    
    if a1+b1<b: #a에서 b로 옮길땐 이것만 고려해주면 된다. 
      func(0,a1+b1)
    else: 
      func(a1-(b-b1),b)

    if a1+c1<c: 
      func(0,b1)
    else:
      func(a1-(c-c1),b1)
      
    if b1+a1<a: #b에서 옮길때
      func(b1+a1,0)
    else:
      func(a,b1-(a-a1))

    if b1+c1<c:
      func(a1,0)
    else:
      func(a1,b1-(c-c1))

    if c1+a1<a: #c에서 옮길때
      func(a1+c1,b1)
    else:
      func(a,b1)

    if c1+b1<b:
      func(a1,b1+c1)
    else:
      func(a1,b)

a,b,c=map(int,input().split())
visit=[[0]*201 for i in range(201)]

result=[]
q=deque()

bfs()
result.sort()
print(' '.join(map(str,result)))


        





