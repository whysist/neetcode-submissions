class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        check=set()
        for i in range(len(nums)):
            if nums[i] in check:
                dup=nums[i]
            check.add(nums[i])
        for i in range(1,len(nums)+1):
            if i not in check:
                rem=i
                break
        return [dup,rem]

        
        