n=int(input())
a=list(map(int,input().split()))
d=[0]*(n)


for i in range(n):
  d[i]=a[i]
  for j in range(0,i):
    if a[i]>a[j]:
      d[i]=max(d[i],d[j]+a[i])

print(max(d))
