n,k=map(int,input().split())
d=[[0 for i in range(201)]for j in range(201)]
mod=1000000000

for i in range(0,201):
  d[1][i]=1
  d[2][i]=i+1
for i in range(0,201):
  d[i][0]=1

for i in range(3,201):
  for p in range(1,201):
    d[i][p]=d[i-1][p]+d[i][p-1]
    d[i][p]%=mod

print(d[k][n])

n,k=map(int,input().split())
# d=[[0 for i in range(201)]for j in range(201)]
# mod=1000000000

# for i in range(0,201):
#   d[1][i]=1
#   d[2][i]=i+1
# for i in range(0,201):
#   d[i][0]=1

# for i in range(3,201):
#   for p in range(1,201):
#     for j in range(0,p+1):
#       d[i][p]+=d[i-1][j]
#     d[i][j]%=mod

# print(d[k][n])
  



