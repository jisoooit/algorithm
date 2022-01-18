N, S = map(int, input().split())
arr = list(map(int, input().split()))

start, end=0,0
tot=0
m=100001
while True:
  if tot<S:
    if end==N:
      break;
    tot+=arr[end]
    end+=1
  else:
    m=min(m,end-start)
    tot-=arr[start]
    start+=1
print(m if m!=100001 else 0)
