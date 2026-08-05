class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check={x:i for i,x in enumerate(nums)}
        for j,y in enumerate(nums):
            if (target-y) in check and check[(target-y)]!=j:
                return [check[(target-y)],j] if check[(target-y)]<j else [j,check[(target-y)]]
        


        