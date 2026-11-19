class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diag=0
        n=len(mat)
        for i in range(n):
            diag+=mat[i][i]
            diag+=mat[i][n-i-1]

        return diag-(mat[n//2][n//2] if n%2 else 0)