class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        if len(heights)==1:
            return 0
        exp=sorted(heights)
        ans=0
        for x,y in zip(exp,heights):
            if x!=y:
                ans+=1
        return ans
        