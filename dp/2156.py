n=int(input())
g=[]
d=[0]*(n)
for i in range(n):
  g.append(int(input()))

for i in range(n):
  if i==0:
    d[i]=g[i]
  elif i==1:
    d[i]=g[1]+g[2]
  elif i==2:
    d[i]=max(d[0]+g[2],d[1]+g[2],g[1]+g[2])
  else:
    d[i]=max(g[i-1]+d[i-3],d[i-2])+g[i]
    d[i]=max(d[i],d[i-1])

print(d[n-1])
