from collections import deque

def bfs(): #비어있는 칸을 x,y로 하자
  q=deque()
  q.append(start)
  while q:
    now=q.popleft()
    if now=="123456789":
      return cntdict[now]

    #현재 빈칸 위치
    pos=now.find("9")
    y=pos//3
    x=pos%3
    
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if 0<=nx<3 and 0<=ny<3:
        npos=ny*3+nx
        nextn=list(now)
        nextn[npos],nextn[pos]=nextn[pos],nextn[npos]
        nextn="".join(nextn) #다시 문자열로
        if not cntdict.get(nextn):
          q.append(nextn)
          cntdict[nextn]=cntdict[now]+1
    
  
dx=[1,0,-1,0]
dy=[0,1,0,-1]

start=""
for i in range(3):
  temp=input()
  temp=temp.replace(" ","")
  start+=temp

start=start.replace("0","9")

q=deque()
q.append(start)

#배열로 하면 크기 가늠이 힘드니까 키벨류형태인 dict사용하는 듯 하다.
cntdict=dict()
cntdict[start]=0

result=bfs()
print(result if result!=None else "-1")



        





