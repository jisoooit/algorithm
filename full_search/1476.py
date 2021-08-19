e,s,m=map(int,input().split())
ear,sun,moon=0,0,0
if e==15:
  e=0
if s==28:
  s=0
if m==19:
  m=0

while True:
  ear+=1
  sun+=1
  moon+=1
  if ear%15==e and sun%28==s and moon%19==m:
    print(ear)
    break
