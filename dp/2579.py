n=int(input())
a=[]
d=[0]*(n)
for i in range(n):
  a.append(int(input()))

for i in range(0,n):
  if i==0:
    d[i]=a[0]
  elif i==1:
    d[i]=a[0]+a[1]
  elif i==2:
    d[i]=max(a[0]+a[2],a[1]+a[2])
  else:
    d[i]=max(d[i-2]+a[i],d[i-3]+a[i-1]+a[i])


print(d[n-1])
