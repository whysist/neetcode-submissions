from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count=Counter(nums)
        ans=float('-inf')
        for x in nums:
            if count[x]==1:
                ans=max(ans,x)
        return ans if ans!=float('-inf') else -1

        