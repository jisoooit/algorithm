from collections import deque

def bfs():
  q=deque()
  q.append([0,0])
  dist[0][0]=0
  while q:
    x,y=q.popleft()
    
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<M and 0<=ny<N:
        if dist[ny][nx]==-1:
          if maze[ny][nx]==0:
            dist[ny][nx]=dist[y][x]
            q.appendleft([nx,ny])
          else:
            dist[ny][nx]=dist[y][x]+1
            q.append([nx,ny])

          

dx=[1,0,-1,0]
dy=[0,1,0,-1]
M,N=map(int,input().split())
maze=[list(map(int,input())) for i in range(N)]
dist=[[-1]*M for i in range(N)]
bfs()

print(dist[N-1][M-1])
