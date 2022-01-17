from itertools import combinations 

n,s=map(int,input().split())
arr=list(map(int,input().split()))

result=0
for i in range(n):
  com=list(combinations(arr,i+1))
  for cm in com:
    sm=sum(cm)
    if sm==s:
      result=result+1

print(result)
