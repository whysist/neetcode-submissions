class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        minNum=min(nums)
        x=sum(int(ch) for ch in str(minNum))
        return 1 if x%2==0 else 0