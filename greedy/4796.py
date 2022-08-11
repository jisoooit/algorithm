cnt=1
a,b,c=map(int,input().split())
while a!=0 and b!=0 and c!=0:
  res=0
  res=a*(c//b) # c<b인 경우는 자동으로 0이 됨. 
  if c%b<=a:
    res+=c%b
  else:
    res+=a
  print("Case "+str(cnt)+":",res)
  cnt+=1
  a,b,c=map(int,input().split())
