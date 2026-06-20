class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums)==1:
            return 1 if nums[0]>=target else 0
        
        if target==1:
            return 1
        
        currSum=0
        ans=float('inf')
        L=0
        R=-1
        while R<len(nums):
            if currSum<target:
                R+=1
                if (R==len(nums)):break
                currSum+=nums[R]
            else:
                ans=min(ans,R-L+1)
                currSum-=nums[L]
                L+=1
        return ans if ans!=float('inf') else 0

        