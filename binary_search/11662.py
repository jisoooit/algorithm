import math

ax,ay,bx,by,cx,cy,dx,dy=map(float,input().split())

interval=1000000
abx=(bx-ax)/interval
aby=(by-ay)/interval
cdx=(dx-cx)/interval
cdy=(dy-cy)/interval

def getdist(x1,y1,x2,y2):
  return math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))

min=getdist(ax,ay,cx,cy)
for i in range(1,interval+1):
  tmp=getdist(ax+abx*i,ay+aby*i,
  cx+cdx*i,cy+cdy*i)
  if tmp<min:
    min=tmp
  
print(min)
  
