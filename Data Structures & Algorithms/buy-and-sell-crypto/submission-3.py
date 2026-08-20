class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        ans=0
        n=len(prices)
        while l<n-1:
            r=l+1
            while r<n and prices[r]>=prices[l]:
                ans=max(ans,prices[r]-prices[l])
                r+=1
            l=r
        return ans
            
        