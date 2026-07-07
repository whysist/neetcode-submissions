class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        ans=0
        res=0
        LIMIT=5000
        for wt in weight:
            if ans+wt<=5000:
                ans+=wt
                res+=1
        return res

        