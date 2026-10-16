class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1 if nums[0]==0 else 0
        
        i=0
        ans=0
        N=len(nums)
        while i<N:
            if nums[i]==0:
                j=i
                c=0
                while j<N and nums[j]==nums[i]:
                    c+=1
                    j+=1
                i=j
                ans+=((c*(c+1))//2)
            else:
                i+=1
        return ans