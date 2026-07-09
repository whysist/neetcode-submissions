class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        vis=[[False]*n for _ in range(m)]
        def dfs(i,j,c,org):
            if 0<=i<m and 0<=j<n and not vis[i][j] and image[i][j]==org:
                vis[i][j]=True
                image[i][j]=c
                dfs(i+1,j,c,org)
                dfs(i,j+1,c,org)
                dfs(i-1,j,c,org)
                dfs(i,j-1,c,org)
        dfs(sr,sc,color,image[sr][sc])
        return image

        