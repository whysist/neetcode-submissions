class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        nums.sort()
        c=nums[0]
        for num in nums:
            if c==num:
                c+=1
            else:
                return False
        return True