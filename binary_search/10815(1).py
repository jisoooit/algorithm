put())
a=list(map(int,input().split()))
m=int(input())
a2=list(map(int,input().split()))
a3=[]
a.sort()

def binary_search(array,target,start,end):
  while start<=end:
    mid=(start+end)//2
    if array[mid]==target:
      return mid
    elif array[mid]>target:
      end=mid-1
    else:
      start=mid+1
  return None


for i in a2:
  num=binary_search(a,i,0,len(a)-1)
  if num==None:
    a3.append(0)
  else:
    a3.append(1)


for i in a3:
  print(i,end=' ')
