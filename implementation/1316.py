import sys

n = int(sys.stdin.readline().rstrip())
lst = []

cnt=0
for i in range(n):
  flag=True
  lst.append(list(sys.stdin.readline().rstrip()))
  grouplst=[]
  for l in lst[i]:
    if l not in grouplst:
      grouplst.append(l)
    else:
      idx=grouplst.index(l)
      if idx!=len(grouplst)-1:
        flag=False
  if flag==True:
    cnt+=1

print(cnt)
  
