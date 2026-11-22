class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans=nums[0]
        c=1
        for i in range(1,len(nums)):
        
            if nums[i]!=ans:
                c-=1
                if c<0:
                    ans=nums[i]
            else:
                c+=1
        return ans