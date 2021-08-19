n=int(input())
a=list(map(int,input().split()))
m=int(input())
a2=list(map(int,input().split()))

dic=[]
#숫자카드와 개수를 딕셔너리에 담기
for i in a:
  if i in dic:
    dic[i]+=1
  else:
    dic[i]=1

for i in a2:
  if i in dic: #존재하는 숫자카드라면 
    print(dic[i],end=' ')
  else:
    print(0,end=' ')
