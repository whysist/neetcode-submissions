class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def nCr(n,r):
            if r>n: 
                return 0
            if r==0 or r==n: 
                return 1
            if r>n-r:
                r=n-r
            res=1
            for i in range(r):
                res=res*(n-i)//(i+1)
            return res
        
        ans=0
        for j in range(3+1):
            ans+= ((-1)**j)*(nCr(3,j))*nCr(n-j*(limit+1)+2,2)
        return ans