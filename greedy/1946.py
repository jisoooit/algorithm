import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
  n = int(sys.stdin.readline().strip())
  res=1
  people_lst = [0]*n
  for j in range(n) :
    t1 ,t2 = map(int, sys.stdin.readline().split())
    people_lst[j] = [t1,t2]

  plsorted=sorted(people_lst, key=lambda x:x[0])
  interview=plsorted[0][1]
  for j in range(1,n):
    if plsorted[j][1]<interview:
      res+=1
      interview=plsorted[j][1]
  print(res)
