class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minSum=maxSum=currMin=currMax=nums[0]
        total=sum(nums)
        for x in (nums[1:]):
            currMax=max(x,currMax+x)
            maxSum=max(maxSum,currMax)
            currMin=min(x,currMin+x)
            minSum=min(minSum,currMin)
        if maxSum<0:
            return maxSum
        return max(maxSum,total-minSum)