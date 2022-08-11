n=int(input())
arr=[250,60,10]
cnt=[0,0,0]
for i in range(3):
  cnt[i]=n//arr[i]
  n=n%arr[i]


if n!=0:
  print(-1)
else:
  print(cnt[0],cnt[1],cnt[2])
