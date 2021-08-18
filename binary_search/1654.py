k,n=map(int,input().split())
a=[]
for i in range(k):
  a.append(int(input()))

start=1
end=max(a)

result=0
while(start<=end):
  cnt=0
  mid=(start+end)//2
  for i in a:
    cnt+=i//mid
  if cnt<n:
    end=mid-1
  else:
    result=mid
    start=mid+1

print(result)
