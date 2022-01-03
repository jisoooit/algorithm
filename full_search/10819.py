import itertools

n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

arr2=list(itertools.permutations(arr,n))
res=0

for i in arr2:
  cur=0
  for j in range(len(i)-1):
    cur+=abs(i[j]-i[j+1])
  if cur>res:
    res=cur
print(res)
