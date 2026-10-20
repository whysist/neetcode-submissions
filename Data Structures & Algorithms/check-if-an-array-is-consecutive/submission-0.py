class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1]!=(nums[i]+1):
                return False
        return True
