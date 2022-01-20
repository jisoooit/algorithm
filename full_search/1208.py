from collections import defaultdict
from itertools import combinations

n,s=map(int,input().split())
arr=list(map(int,input().split()))

l=arr[:n//2]
r=arr[n//2:]

#dict을 사용한 이유는 같은 값이 연속해서 나왔을때 처리하기 혼란스러워서 아예 같은 값이 하나만 존재하게하기 위함(개수는 value로 측정해주면 되니까)
lsum=defaultdict(int)
rsum=defaultdict(int)

#원소 한개도 합이 될 수 있기 때문에 0을 넣어줬다.
lsum[0]=1 
rsum[0]=1

for i in range(1,len(l)+1):
  for com in combinations(l,i):
    lsum[sum(com)]+=1

for i in range(1,len(r)+1):
  for com in combinations(r,i):
    rsum[sum(com)]+=1

lkey=sorted(lsum.keys())
rkey=sorted(rsum.keys())

res=0
l=0
r=len(rkey)-1
while l<len(lkey) and r>=0:
  if lkey[l]+rkey[r]==s:
    res+=(lsum[lkey[l]]*rsum[rkey[r]]) #여기 더하기가 아니고 곱하기임!!! 당연함
    l+=1
    r-=1
  elif lkey[l]+rkey[r]>s:
    r-=1
  else:
    l+=1

#위에 넣어준 0때문에 s가 0일때 합이 0인게 무조건 1개 잡히므로 -1해줘야 한다.
if s==0:
  res-=1
print(res)
