class Solution:
    def isHappy(self, n: int) -> bool:
        def checkSum(n):
            ans=0
            while n:
                dig=n%10
                dig= dig**2
                ans+=dig
                n=n//10
            return ans

        vis=set()
        while n not in vis:
            vis.add(n)
            n=checkSum(n)
            if n==1:
                return True
        return False
        