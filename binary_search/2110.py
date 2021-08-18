n,c=map(int,input().split())
a=[]
for i in range(n):
  a.append(int(input()))

a.sort()
start=1
end=max(a)-min(a)

result=0
while(start<=end):
  mid=(start+end)//2
  current=a[0]
  cnt=1

  for i in range(1,len(a)):
    if a[i]>=current+mid:
      cnt+=1
      current=a[i]

  if cnt<c:
    end=mid-1
  else:
    result=mid
    start=mid+1

print(result)
