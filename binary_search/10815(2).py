n=int(input())
a=set(input().split())
m=int(input())
a2=list(input().split())
a3=[]
for i in a2:
  if i in a:
    a3.append(1)
  else:
    a3.append(0)

for i in a3:
  print(i,end=' ')
