class Solution:
    def isUgly(self, n: int) -> bool:
        if n==1:
            return True
        pfs=[2,3,5]
        for pf in pfs:
            while n%pf==0:
                n//=pf
        
        return n==1       