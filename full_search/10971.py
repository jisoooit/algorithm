import itertools

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
arr2=[j for j in range(n)]

res=10000000
a=arr2.copy()
a.remove(0)
per=list(itertools.permutations(a,n-1))
for j in per:
 j=[*j]
 j=[0]+j+[0]
 s=0
 for i in range(len(j)-1):
   cost=arr[j[i]][j[i+1]]
   if cost==0:
     break
   else:
     s+=cost
   
   if s>res:
     break
    
 else:
   if res>s:
       res=s
 

print(res)
