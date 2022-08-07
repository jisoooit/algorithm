n=int(input())
arr=[]
for i in range(n):
  arr.append(int(input()))
arr.sort(reverse=True)

res=0
for i in range(n):
  if res<arr[i]*(i+1):
    res=arr[i]*(i+1)
print(res)
