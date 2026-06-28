class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        total=sum(nums)
        lS=0
        for i in range(len(nums)):
            rS=total-lS-nums[i]
            if lS==rS:
                return i
            lS+=nums[i]
        return -1