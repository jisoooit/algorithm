import math

N = int(input())
arr=[True for i in range(N+1)] #처음에 모두 소수로 놓음
arr[0],arr[1]=False,False
arr2=[]

for i in range(2,int(math.sqrt(N)+1)):
  if arr[i]==True:
    j=2
    while i*j<=N:
      arr[i*j]=False
      j+=1

arr2=[x for x in range(N+1) if arr[x]]



start, end=0,0
tot=0
cnt=0
while True:
  if tot<N:
    if end==len(arr2):
      break
    tot+=arr2[end]
    end+=1
  else:
    if tot==N:
      cnt+=1
    tot-=arr2[start]
    start+=1

print(cnt)
