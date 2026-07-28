class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums)==2:
            return nums
        
        check=set()
        for x in nums:
            if x not in check:
                check.add(x)
            else:
                check.remove(x)
        return list(check)

        