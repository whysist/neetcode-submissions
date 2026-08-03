from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        num_pairs=len(nums)//2
        count=Counter(nums)
        if len(count)==len(nums):
            return False
        
        for x in count:
            if count[x]%2!=0:
                return False
        return True
