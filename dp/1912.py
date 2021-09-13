n=int(input())
a=list(map(int,input().split()))
d=[0]*(n)

d[0]=a[0]
#d[1]=max(d[0]+a[1],a[1])
for i in range(1,n):
  d[i]=max(a[i],d[i-1]+a[i])

print(max(d))
