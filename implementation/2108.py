from collections import Counter

n=int(input())
arr=[0]*n
for i in range(n):
  arr[i]=int(input())

arr.sort()

#최빈값 구하기
cnt=Counter(arr)
mc=cnt.most_common()

mclist=[]
maxnum=mc[0][1]
for m in mc:
  if maxnum==m[1]:
    mclist.append(m[0])

    
print(round(sum(arr)/n))
print(arr[n//2])
print(mclist[1] if len(mclist)>1 else mclist[0])
print(abs(max(arr)-min(arr)))
