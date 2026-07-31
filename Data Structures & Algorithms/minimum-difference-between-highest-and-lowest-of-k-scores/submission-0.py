class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        ans=float('inf')
        for i in range(n-k+1):
            window=nums[i:i+k]
            diff=window[-1]-window[0]
            ans=min(ans,diff)
        return ans

        