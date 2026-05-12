from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        q=deque()
        minutes=0
        fresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
            
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        
        while fresh>0 and q:
            length=len(q)
            for i in range(length):
                r,c=q.popleft()
                for dr,dc in dirs:
                    nr,nc=dr+r,dc+c
                    if(nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        q.append((nr,nc))
                        fresh-=1
            minutes+=1
        
        return minutes if fresh==0 else -1
        