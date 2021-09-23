n=int(input())
a=list(map(int,input().split()))
d=[0]*(n+1)
a=[0]+a

for i in range(1,n+1):
  d[i]=a[i]
  for j in range(n+1):
    d[i]=max(d[i],d[j]+d[i-j])

print(d[n])


