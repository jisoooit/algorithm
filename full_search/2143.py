from itertools import combinations
from collections import defaultdict

t=int(input())
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))


lsum=defaultdict(int)
rsum=defaultdict(int)

#a,b의 연속배열 구해서 dict의 key에 넣고 개수 세기
for i in range(n):
  s=0
  for j in range(i,n):
    s+=a[j]
    lsum[s]+=1

for i in range(m):
  s=0
  for j in range(i,m):
    s+=b[j]
    rsum[s]+=1


lkey=sorted(lsum.keys())
rkey=sorted(rsum.keys())

l=0
r=len(rkey)-1
res=0

while l<len(lkey) and r>=0:
  if lkey[l]+rkey[r]==t:
    res+=lsum[lkey[l]]*rsum[rkey[r]]
    l+=1
    r-=1
  elif lkey[l]+rkey[r]>t:
    r-=1
  else:
    l+=1

print(res)
