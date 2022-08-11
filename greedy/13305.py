n=int(input())
load=list(map(int,input().split()))
oil=list(map(int,input().split()))

res=0
pre=0
m=oil[0]
for i in range(n-1):
  if m>oil[i]:
    m=oil[i]
  res+=m*load[i]
    

print(res)
