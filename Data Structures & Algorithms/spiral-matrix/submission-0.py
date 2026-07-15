class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        top,left,right,bottom=0,0,n-1,m-1
        res=[]
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                res.append(mat[top][i])
            top+=1
            for i in range(top,bottom+1):
                res.append(mat[i][right])
            right-=1
            if top<=bottom and left<=right:
                for i in range(right,left-1,-1):
                    res.append(mat[bottom][i])
                bottom-=1
                for i in range(bottom,top-1,-1):
                    res.append(mat[i][left])
                left+=1
        return res