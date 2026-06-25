class Solution:
    def maxArea(self, nums: List[int]) -> int:
        if len(nums)==2:
            return min(nums[0],nums[1])
        n=len(nums)
        l=0
        r=n-1
        ans=float('-inf')
        while l<r:
            ans=max(ans,(min(nums[l],nums[r])*(r-l)))
            # print(ans)
            if nums[l]>nums[r]:
                r-=1
            else:
                l+=1
        return ans

        