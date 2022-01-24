n=int(input())
al,bl,cl,dl=[],[],[],[]
for _ in range(n):
 a,b,c,d=map(int,input().split())
 al.append(a)
 bl.append(b)
 cl.append(c)
 dl.append(d)

ab=dict()

#a랑 b배열에서 나올 수 있는 합 모두 구하기
for a in al:
  for b in bl:
    ab[a+b]=ab.get(a+b,0)+1

res=0
for c in cl:
  for d in dl:
   res+=ab.get(-(c+d),0)


print(res)
