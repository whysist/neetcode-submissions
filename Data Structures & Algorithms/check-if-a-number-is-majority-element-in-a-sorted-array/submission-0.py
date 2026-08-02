class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        c=0
        for x in nums:
            if x==target:
                c+=1
        return True if c>(len(nums)/2) else False
        