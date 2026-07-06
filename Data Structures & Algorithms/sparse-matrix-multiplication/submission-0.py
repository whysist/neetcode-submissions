class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m,n=len(mat1),len(mat1[0])
        a,b=len(mat2),len(mat2[0])
        ans=[[0 for _ in range(b)] for _ in range(m)]
        for i in range(m):
            for j in range(b):
                for k in range(n):
                    ans[i][j]+=mat1[i][k]*mat2[k][j]
        return ans

        