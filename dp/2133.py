n=int(input())
d=[0]*(n+1)

for i in range(1,n+1):
  if i==1:
    d[1]=0
  elif i==2:
    d[2]=3
  elif i%2==0:
    d[i]=3*d[i-2]+2
    for j in range(i-4,0,-2):
      d[i]+=2*d[j]

print(d[n])

