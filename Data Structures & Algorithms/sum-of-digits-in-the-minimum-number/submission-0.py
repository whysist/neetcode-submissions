class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        minNum=min(nums)
        x=0
        while minNum:
            dig=minNum%10
            x+=dig
            minNum//=10
        return 1 if x%2==0 else 0