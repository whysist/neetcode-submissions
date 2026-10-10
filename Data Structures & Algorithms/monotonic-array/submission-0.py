class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        checkMono=checkDec=True
        for i in range(1,len(nums)):
            if nums[i]>=nums[i-1]:
                continue
            else:
                checkMono=False
                break
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                continue
            else:
                checkDec=False
                break
        return (checkMono or checkDec)
        