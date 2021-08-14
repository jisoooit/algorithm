import math


n,p=input().split()

d=[0]
d.append(n)
while True:
  n=str(sum(int(c)**int(p)for c in n))
  if n in d:
    print(d.index(n)-1)
    break
  d.append(n)
