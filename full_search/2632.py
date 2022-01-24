from collections import deque
from collections import defaultdict

p=int(input())
m,n=map(int,input().split())
a,b=[],[]
for i in range(m):
  a.append(int(input()))
for i in range(n):
  b.append(int(input()))

da=deque(a)
db=deque(b)


lsum=defaultdict(int)
rsum=defaultdict(int)
lsum[0]=1
rsum[0]=1
for i in range(m):
  s=0
  for j in range(0,m):
    s=s+da[j]
    lsum[s]+=1
  da.rotate(-1)

lsum[sum(a)]-=m-1

for i in range(n):
  s=0
  for j in range(0,n):
    s+=db[j]
    rsum[s]+=1
  db.rotate(-1)

rsum[sum(b)]-=n-1

lkey=sorted(lsum.keys())
rkey=sorted(rsum.keys())

l=0
r=len(rkey)-1
res=0
while l<len(lkey) and r>=0:
  if lkey[l]+rkey[r]==p:
    res+=lsum[lkey[l]]*rsum[rkey[r]]
    l+=1
    r-=1
  elif lkey[l]+rkey[r]>p:
    r-=1
  else:
    l+=1

print(res)
