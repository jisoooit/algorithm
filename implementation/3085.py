import sys
from itertools import groupby

n = int(sys.stdin.readline().rstrip())
lst = []
for i in range(n):
    lst.append(list(sys.stdin.readline().rstrip()))


def checkcol(j): # j열에서 가장 긴 문자 길이
  colist=list(zip(*lst))[j] #j열을 리스트로 
  return max([len(list(g)) for k, g in groupby(''.join(colist))], default=0)

def checkrow(i): # i행에서 가장 긴 문자 길이
  return max([len(list(g)) for k, g in groupby(lst[i])], default=0)

cnt=0
for i in range(n):
  for j in range(n):
    if j+1<n and lst[i][j]!=lst[i][j+1]:
      lst[i][j],lst[i][j+1]=lst[i][j+1],lst[i][j] # 문자 다르면 바꿈
      cnt=max(cnt,checkcol(j+1))
      cnt=max(cnt,checkcol(j))
      cnt=max(cnt,checkrow(i))
      lst[i][j],lst[i][j+1]=lst[i][j+1],lst[i][j] # 바꿨을때 cnt들 구하고 다시 원래대로 리턴
    else:
      cnt=max(cnt,checkcol(j))
      cnt=max(cnt,checkrow(i))
    if i+1<n and lst[i][j]!=lst[i+1][j]:
      lst[i][j],lst[i+1][j]=lst[i+1][j],lst[i][j]
      cnt=max(cnt,checkcol(j))
      cnt=max(cnt,checkrow(i))
      cnt=max(cnt,checkrow(i+1))
      lst[i][j],lst[i+1][j]=lst[i+1][j],lst[i][j]
    else:
      cnt=max(cnt,checkcol(j))
      cnt=max(cnt,checkrow(i))
      
print(cnt)
