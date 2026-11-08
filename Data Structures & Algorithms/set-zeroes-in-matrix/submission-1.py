class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroes=set()
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    zeroes.add((i,j))
        # print(zeroes)
        for row,col in zeroes:
            for j in range(n):
                matrix[row][j]=0
            for k in range(m):
                matrix[k][col]=0
        
                
        
        