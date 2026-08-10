class Solution:
    def maxArea(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,n-1
        ans=0
        while l<r:
            ans=max(ans,(min(nums[r],nums[l]))*(r-l))
            if nums[l]>nums[r]:
                r-=1
            else:
                l+=1
        return ans


        