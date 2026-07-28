class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        ans=0
        for x in nums:
            ans= ans^x
        return ans
        