class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        a,b=nums[0],nums[1]
        c,d=nums[n-1],nums[n-2]
        return (c*d)-(a*b)
