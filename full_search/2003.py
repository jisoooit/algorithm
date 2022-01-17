n,m=map(int,input().split())
arr=list(map(int,input().split()))

end=0
cnt=0
tot=0
for start in range(len(arr)):
  while tot<m and end<len(arr):
    tot+=arr[end]
    end+=1
  if tot==m:
    cnt+=1
  tot-=arr[start]

print(cnt)
