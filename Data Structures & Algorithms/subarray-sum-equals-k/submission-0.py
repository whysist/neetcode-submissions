class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return 1 if nums[0]==k else 0
        n=len(nums)
        res=0
        curSum=0
        prefixSums={0:1}
        for num in nums:
            curSum+=num
            diff=curSum-k
            res+= prefixSums.get(diff,0)
            prefixSums[curSum]=1+prefixSums.get(curSum,0)
        return res