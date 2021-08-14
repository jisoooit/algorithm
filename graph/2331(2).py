import math


n,p=map(int,input().split())

d=[0]
d.append(n)
i=2
dcan=0
while True:
  a=int(d[i-1])
  while a!=0:
    dcan+=int(math.pow(a%10,p))
    a//=10
  if dcan in d:
    print(d.index(dcan)-1)
    break
  d.append(dcan)
  dcan=0
  i+=1
