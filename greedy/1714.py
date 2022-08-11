import sys
import heapq

hp=[]

n=int(sys.stdin.readline().strip())
for i in range(n):
  heapq.heappush(hp,int(sys.stdin.readline().strip()))
  
res=0
if n>1: #n==1일때 인덱스 에러 남. 
  while True:
    a=heapq.heappop(hp)
    b=heapq.heappop(hp)
    c=a+b
    res+=c
    if len(hp)==0:
      break
    heapq.heappush(hp,c)
else:
  res=0
print(res)
