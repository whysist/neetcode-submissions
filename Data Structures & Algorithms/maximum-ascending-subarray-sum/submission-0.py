class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        currSum,ans=nums[0],nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                currSum+=nums[i]
                ans=max(ans,currSum)
            else:
                currSum=nums[i]
        return ans