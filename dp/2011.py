a=[]
num=input()
for i in num:
  a.append(int(i))
n=len(a)
d=[0]*(n+1)

if a[0]==0:
  print(0)
else:
  #인덱스 맞추기 위해서 0삽입
  a=[0]+a
  d[0]=1
  d[1]=1
  for i in range(2,n+1):
    if 10<=a[i-1]*10+a[i]<=26:
      d[i]+=d[i-2]
    if 1<=a[i]<=9:
      d[i]+=d[i-1]
    d[i]%=1000000
  print(d[n])



