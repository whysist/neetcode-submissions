class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchRow(row,l,r):
            if l>r:
                return False
            mid=(l+r)//2
            if row[mid]<target:
                return searchRow(row,mid+1,r)
            elif row[mid]>target:
                return searchRow(row,l,mid-1)
            else:
                return True
        
        top=0
        bottom=len(matrix)-1
        r=len(matrix[0])-1
        while top<=bottom: 
            mid=(top+bottom)//2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]<=target and matrix[mid][r]>=target:
                return searchRow(matrix[mid],0,r)
            elif matrix[mid][0]<target:
                top=mid+1
            else:
                bottom=mid-1
        
        return False
                
