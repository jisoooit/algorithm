from itertools import combinations 

while(True):
  arr=list(map(int,input().split()))
  k=arr[0];
  s=arr[1:];
  if k==0:
    break; 
  com=list(combinations(s,6));
  for c in com:
    for i in c:
      print(i,end=' ')
    print()
  print()
