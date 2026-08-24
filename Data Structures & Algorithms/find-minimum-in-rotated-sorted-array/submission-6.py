class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        r=n-1
        ans=nums[0]
        while l<=r:
            if nums[l]<nums[r]:
                ans=min(ans,nums[l])
                break
            m=(l+r)//2
            ans=min(ans,nums[m])
            if nums[l]<=nums[m]:
                l=m+1
            else:
                r=m-1
        return ans

        