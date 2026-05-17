from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo=defaultdict(int)
        res=[]
        for i in range(len(nums)):
            num=nums[i]
            if target-num in memo:
                res.append(memo[target-num])
                res.append(i)
                break
            else:
                memo[num]=i
        return res