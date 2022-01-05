from collections import deque
import math
t=int(input())

visit=[0]*(10000)
def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True # 소수임

def bfs(n_list):
  q=deque()
  q.append(n_list)
  while q:
    num=q.popleft()
    num2=num[:]
    n_num=int(''.join(map(str, num)))
    if n_num==m:
      return visit[n_num]
    for j in range(4):
      for i in range(10):
        if(num2[j]!=i):
          if(j==0):
            if(i!=0):
              num2[j]=i
            else:
              continue
          else:
            num2[j]=i
        else:
          continue
        n_num2=int(''.join(map(str, num2)))
        if is_prime(n_num2) and visit[n_num2]==0: #여기서 1000이상인것만 걸러도 ok
          q.append(num2)
          visit[n_num2]=visit[n_num]+1
        num2=num[:]
  return "impossible"

for i in range(t):
  n,m=map(int,input().split())
  n_list = list(map(int, str(n)))
  print(bfs(n_list))
  visit=[0]*(10000)
