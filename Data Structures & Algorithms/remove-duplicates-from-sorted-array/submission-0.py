class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        unique=sorted(set(nums))
        nums[:len(unique)]=unique
        return len(unique)
    



        