t=int(input())
for i in range(t):
  n=int(input())
  d=[[0 for i in range(n)] for j in range(2)]
  s=[]
  for j in range(2):
    s.append(list(map(int,input().split())))
  
  d[0][0],d[1][0]=s[0][0],s[1][0]

  for i in range(1,n):
    for j in range(2):
      if j==0:
        d[0][i]+=max(d[0][i-1], d[1][i-1]+s[0][i])
      elif j==1:
        d[1][i]+=max(d[1][i-1], d[0][i-1]+s[1][i])
  # for i in range(2):
  #   for j in range(1,n):
  #     if i==0:
  #       d[0][j]+=max(d[0][j-1], d[1][j-1]+s[0][j])
  #     elif i==1:
  #       d[1][j]+=max(d[1][j-1], d[0][j-1]+s[1][j])
  print(max(d[0][n-1],d[1][n-1]))
