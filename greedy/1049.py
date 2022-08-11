n,m=map(int,input().split())
glist=[list(map(int,input().split())) for _ in range(m)]


set=1000
one=1000
for i in range(m):
  if set>glist[i][0]:
    set=glist[i][0]
  if one>glist[i][1]:
    one=glist[i][1]

res=0
share=n//6
rest=n%6
if set<6*one:
  res+=set*share
else:
  res+=6*one*share
if set<rest*one:
  res+=set
else:
  res+=one*rest
print(res)
