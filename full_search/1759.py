from itertools import combinations 

l,c=map(int,input().split())
items=sorted(list(input().split()))

com=list(combinations(items, l))
com.sort()
#정렬을 미리 해주면 편해진다.


for cm in com:
  vow=0
  for i in cm:
    if i in "aeiou":
      vow+=1
    
  if vow>=1 and l-vow>=2:
    print(''.join(cm))
