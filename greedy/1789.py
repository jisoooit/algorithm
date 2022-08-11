n=int(input())
arr=[]
num=0
s=1
while True:
  num+=s
  s+=1
  if num>n:
    s-=1  # s-1 을 cnt로 생각했다. 넘어가면 cnt-1해줘야한다. 
    break


print(s-1)
