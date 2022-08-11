A,B=map(int,input().split())


res=0
Flag=False
while B>=A:
  if B==A:
    Flag=True
    break
  if B%2==0:
    B=B//2
    res+=1
  else:
    if B%10==1:
      B=B//10
      res+=1
    else:
      break

print(res+1 if Flag else -1)
