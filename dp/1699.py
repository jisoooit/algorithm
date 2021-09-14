import math

n=int(input())
d=[0]*(n+1)


for i in range(n+1):
  d[i]=i
for i in range(4,n+1):
  num=0
  for j in range(1,int(math.sqrt(i))+1):
    num=int(math.pow(j,2))
    d[i]=min(1+d[i-num],d[i])

print(d[n])



