n=int(input())
d=[[0 for i in range(10)] for j in range(1001)]

for i in range(10):
  d[1][i]=1
for i in range(2,n+1):
  for j in range(10):
    for k in range(0,j+1):
      d[i][j]+=d[i-1][k]

print(sum(d[n])%10007)
