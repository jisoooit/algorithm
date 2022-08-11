import sys


s=sys.stdin.readline().strip()

cnt=[0,0]
cnt[int(s[0])]+=1

for i in range(1,len(s)):
  if s[i-1]!=s[i]:
    cnt[int(s[i])]+=1

res=0
res= cnt[0] if cnt[0]<cnt[1] else cnt[1]
print(res)
