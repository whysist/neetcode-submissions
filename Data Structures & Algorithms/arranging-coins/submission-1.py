class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==1:
            return 1
        l=0
        r=n
        ans=None
        while l<=r:
            mid=(l+r)//2
            cum_sum= ((mid)*(mid+1))//2
            if cum_sum==n:
                return mid
            elif cum_sum<=n:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
            