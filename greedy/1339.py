import sys
from collections import defaultdict

intdict=defaultdict(int)

n=int(sys.stdin.readline().strip())
arr=[0]*n
maxlen=0

for i in range(n):
  arr[i]=sys.stdin.readline().strip()
  if len(arr[i])>maxlen:
    maxlen=len(arr[i])

num=9

for a in arr: # 알파벳 별 자릿수 더하기
  for i,s in enumerate(a):
    intdict[s]+=10**(len(a)-i)


alphasort=sorted(intdict, key=lambda x:intdict[x], reverse=True) #자릿수 많은 순서대로 알파벳 정렬


for i in range(len(alphasort)):
  intdict[alphasort[i]]=num #알파벳에 숫자 배정
  num-=1
     

for s in alphasort:
  for i,a in enumerate(arr):
    a=a.replace(s,str(intdict[s]))
    arr[i]=a


res=0
for a in arr:
  res+=int(a)
print(res)
