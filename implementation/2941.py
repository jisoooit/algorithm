s=input()
arr=['dz=','lj','nj','c=','c-','d-','s=','z='] - 3자리 수 앞에 적음
res=0

for i in arr:
  if i in s:
    cnt=s.count(i)
    # res+=cnt 
    s=s.replace(i," ") #"" 안하고 " "한 이유 nljj에서 lj가 삭제되고 nj가 붙는 것을 방지하기 위해. 그래서 바꿀때마다 " "가 추가되고 이 개수가 곧 arr에 포함된 알파벳 이기도 하다. 
    # res-=cnt
    print(s)

res+=len(s)
print(len(s))
print(res)
