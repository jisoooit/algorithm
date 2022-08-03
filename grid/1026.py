n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
bd=dict(zip(range(0,len(b)),b))
bindex=sorted(bd, key=lambda x:bd[x], reverse=True)

answer=0
for i in range(n):
  answer+=sorted(a)[i]*b[bindex[i]]

print(answer)
