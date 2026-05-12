from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        dirs=[(0,1),(0,-1),(-1,0),(1,0)]
        ans=0
        def bfs(i,j):
            q=deque()
            grid[i][j]="0"
            q.append((i,j))
            while q:
                r,c=q.popleft()
                for dr,dc in dirs:
                    nr,nc=dr+r,dc+c
                    if (nr<0 or nc<0 or nr>=m or nc>=n or grid[nr][nc]=="0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc]="0"
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    bfs(i,j)
                    ans+=1
        return ans
        
                
        